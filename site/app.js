/* How AI Learns — plain, dependency-free site behavior.
 * Everything is local; no network calls, no tracking. */

(function () {
  "use strict";

  /* ---- Glossary: live filter on glossary.html ---- */
  var search = document.getElementById("glossary-search");
  var list = document.getElementById("glossary-list");
  var emptyNote = document.getElementById("no-results");

  if (search && list && emptyNote) {
    var entries = Array.prototype.slice.call(list.children);
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      var visible = 0;
      entries.forEach(function (entry) {
        var text = entry.textContent.toLowerCase();
        var show = q === "" || text.indexOf(q) !== -1;
        entry.classList.toggle("hidden", !show);
        if (show) visible += 1;
      });
      emptyNote.classList.toggle("hidden", visible > 0);
    });
  }

  /* ---- Flip cards: the hallucination demos on journey.html ---- */
  Array.prototype.forEach.call(
    document.querySelectorAll(".flip-btn"), function (btn) {
      btn.addEventListener("click", function () {
        btn.classList.toggle("flipped");
        var back = btn.querySelector(".flip-back");
        var front = btn.querySelector(".flip-front");
        if (!back || !front) { return; }
        var showingBack = !back.classList.contains("hidden");
        back.classList.toggle("hidden", showingBack);
        front.classList.toggle("hidden", !showingBack);
      });
    });

  /* ---- Temperature dial (journey.html) ---- */
  var tempSlider = document.getElementById("temp-slider");
  var tempValue = document.getElementById("temp-value");
  var tempOutput = document.getElementById("temp-output");
  var renderCandidates;

  if (tempSlider && tempValue) {
    tempSlider.addEventListener("input", function () {
      tempValue.textContent = tempSlider.value;
      var t = parseFloat(tempSlider.value);
      if (tempOutput) {
        if (t < 0.6) {
          tempOutput.textContent = "Low: the starchy kitchen helper — " +
            "nearly always serves the menu's top dish. Safe for " +
            "fact slots, dull for poems.";
        } else if (t <= 1.2) {
          tempOutput.textContent = "Around 1.0: picks along the menu in " +
            "its usual proportions. This is where the toy was trained.";
        } else {
          tempOutput.textContent = "High: the restless poet happily " +
            "walks down-menu. Vivid words, and occasionally words that " +
            "were never the truth — the seed of confident inventions.";
        }
      }
      if (renderCandidates) { renderCandidates(); }
    });
  }

  /* ---- Toy next-word predictor (journey.html) ----
   * A tiny bigram model built from a fictional "cafe cookbook."
   * Guess → count → nudge is the training loop of chapter 02;
   * this toy does all the counting up front and serves the ranked
   * menu at guess time. The temperature dial re-weights the menu,
   * exactly like the seasoning story in chapter 03. */

  var cafeCookbook = [
    "fresh coffee brews slowly in the morning kitchen",
    "the morning kitchen fills with the smell of fresh bread",
    "fresh bread warms slowly in the oven",
    "the smell of fresh coffee warms the morning kitchen",
    "coffee brews slowly in a fresh pot",
    "the oven warms slowly while the kitchen fills",
    "a warm pot brews fresh coffee for the counter",
    "the counter fills with warm bread in the morning",
    "fresh coffee fills the counter in the morning",
    "the morning cook warms a fresh pot of coffee",
    "bread warms in the oven while coffee brews",
    "the kitchen cook brews fresh coffee slowly",
    "a smell of warm bread fills the kitchen",
    "the oven brews fresh warmth in the morning kitchen"
  ];

  /* Build bigram counts: the menu of next words after every word. */
  var bigrams = {};
  var startWords = {};
  cafeCookbook.forEach(function (line) {
    var words = line.split(" ");
    if (!startWords.hasOwnProperty(words[0])) { startWords[words[0]] = 0; }
    startWords[words[0]] += 1;
    for (var i = 0; i < words.length - 1; i += 1) {
      var key = words[i], next = words[i + 1];
      if (!bigrams.hasOwnProperty(key)) { bigrams[key] = {}; }
      if (!bigrams[key].hasOwnProperty(next)) { bigrams[key][next] = 0; }
      bigrams[key][next] += 1;
    }
  });

  function menuFor(context) {
    var word = (context || "").trim().toLowerCase().split(" ").pop();
    if (!word) {
      return Object.keys(startWords).map(function (w) {
        return { word: w, count: startWords[w] };
      });
    }
    var counts = bigrams[word];
    if (!counts) { return []; }
    return Object.keys(counts).map(function (w) {
      return { word: w, count: counts[w] };
    });
  }

  /* Temperature: lower sharpens the menu, higher flattens it. */
  function weightedPicks(context) {
    var menu = menuFor(context);
    if (!menu.length) { return []; }
    var t = (tempSlider && tempSlider.value)
      ? parseFloat(tempSlider.value) : 1.0;
    var max = Math.max.apply(null, menu.map(function (m) { return m.count; }));
    var weights = menu.map(function (m) {
      return Math.pow(m.count / max, 1.0 / Math.max(t, 0.05));
    });
    var total = weights.reduce(function (a, b) { return a + b; }, 0);
    return menu.map(function (m, i) {
      return { word: m.word, share: weights[i] / total };
    });
  }

  function renderMenu(context) {
    var holder = document.getElementById("nextword-candidates");
    if (!holder) { return; }
    var picks = weightedPicks(context);
    var out;
    if (!picks.length) {
      out = '<p class="hint-text">The toy cookbook has no page with "' +
        context + '" in it. A real model meets the same wall far less ' +
        "often — it read a whole library. Try: fresh, coffee, morning, " +
        "kitchen, bread, the, in.</p>";
    } else {
      picks.sort(function (a, b) { return b.share - a.share; });
      out = picks.slice(0, 6).map(function (p) {
        var pct = Math.round(p.share * 100);
        return '<div class="candidate"><span class="word">' + p.word +
          '</span><span class="bar-track"><span class="bar" style="width:' +
          pct + '%"></span></span><span class="share">' + pct +
          '%</span></div>';
      }).join("");
    }
    holder.innerHTML = out;
  }

  /* ---- Wire the form, starters, and dial together ---- */
  var nwForm = document.getElementById("nextword-form");
  var nwInput = document.getElementById("nextword-input");
  var lastContext = nwInput ? nwInput.value.trim() : "";

  renderCandidates = function () {
    renderMenu(lastContext);
  };

  if (nwForm && nwInput) {
    nwForm.addEventListener("click", function () {
      lastContext = nwInput.value.trim();
      renderMenu(lastContext);
    });
    nwInput.addEventListener("keydown", function (evt) {
      if (evt.key === "Enter") {
        lastContext = nwInput.value.trim();
        renderMenu(lastContext);
      }
    });
  }

  Array.prototype.forEach.call(
    document.querySelectorAll(".starter"), function (btn) {
      btn.addEventListener("click", function () {
        if (!nwInput) { return; }
        nwInput.value = btn.getAttribute("data-start") || "";
        lastContext = nwInput.value;
        renderMenu(lastContext);
      });
    });
  renderCandidates();

  /* ---- Name decoder (names.html) ---- */
  var decoderForm = document.getElementById("decoder-form");
  var decoderInput = document.getElementById("decoder-input");
  var decoderOutput = document.getElementById("decoder-output");

  var decodeCards = {
    "checkers": {
      family: "Checkers — a fictional family; its tone and recipe are its own.",
      size: "7B — seven billion adjustable settings: the everyday laptop class, good manners, decent recall.",
      flavor: "Talk — finished school: answers questions instead of continuing text. Start here for chat.",
      version: "v2 — the second vintage: the whole schooling was re-run on fresher, larger text."
    },
    "checkers-base": {
      family: "Checkers — the same fictional family.",
      size: "7B — seven billion settings, everyday laptop class.",
      flavor: "No suffix — this is the base: the raw library guest. It continues text brilliantly and may babble instead of answering. Legitimate — and not what a chat window wants.",
      version: "No vintage shown: one edition so far."
    },
    "checkers-70": {
      family: "Checkers — the same fictional family.",
      size: "70B — ten times the dials: deeper recall and more nuance, on serious hardware.",
      flavor: "Talk — finished school.",
      version: "v2 — second vintage."
    },
    "checkers-think": {
      family: "Checkers — the same fictional family.",
      size: "7B — everyday laptop class.",
      flavor: "Talk + Think — finished school, then extra training in writing working notes before the final answer. Slow and methodical; overkill for a friendly email.",
      version: "v2 — second vintage."
    },
    "widget-mini": {
      family: "Widget — a different fictional family, different house seasoning.",
      size: "mini — a marketing label: the small, fast, cheap member of the family. A price class, not a promise.",
      flavor: "Marketing label, not a school label: check the product page to know whether this one finished school (almost certainly yes, if it's in a chat picker).",
      version: "4 — fourth vintage of the Widget family."
    }
  };

  if (decoderForm && decoderInput && decoderOutput) {
    decoderForm.addEventListener("click", function () {
      var chosen = decodeCards[decoderInput.value];
      if (!chosen) { return; }
      var name = decoderInput.options[decoderInput.selectedIndex].textContent;
      decoderOutput.innerHTML =
        '<p class="hint-text">Decoding <strong>' + name + '</strong>:</p>' +
        '<table><thead><tr><th>Piece</th><th>Reading</th></tr></thead>' +
        '<tbody>' +
        '<tr><td><strong>Family</strong></td><td>' + chosen.family +
        '</td></tr>' +
        '<tr><td><strong>Size</strong></td><td>' + chosen.size +
        '</td></tr>' +
        '<tr><td><strong>Flavor</strong></td><td>' + chosen.flavor +
        '</td></tr>' +
        '<tr><td><strong>Version</strong></td><td>' + chosen.version +
        '</td></tr>' +
        '</tbody></table>';
    });
  }
})();
