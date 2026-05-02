const ext = function () {
    var BotNames = [
	    "LeelaKnightOdds",
	    "LeelaRookOdds",
	    "LeelaQueenOdds",
	    "LeelaQueenForKnight",
	    "LeelaPieceOdds",
	    "LeelaPieceOddsFRC",
    ];

    var MoveStatURL = "http://localhost:5000/";
    function AddMoveStats() {
	    console.log("Adding move stats");
	    var computer = document.querySelector("div[role=tablist] button[role=tab].computer-analysis");
	    var tabPanel = document.querySelector("div.analyse__underboard__panels");
	    if (!computer || !tabPanel) {
		    console.log("Computer analysis tab not found");
		    return;
	    }
	    var white = document.querySelector("aside.analyse__side div.player.white a.user-link");
	    var black = document.querySelector("aside.analyse__side div.player.black a.user-link");
	    if (!white || !black) {
		    console.log("Player links not found");
		    return;
	    }

	    var whiteName = white.href.split("/")[4];
	    var blackName = black.href.split("/")[4];
	    var isWhiteBot = BotNames.includes(whiteName);
	    var isBlackBot = BotNames.includes(blackName);

	    if (!isWhiteBot && !isBlackBot) {
		    console.log("No bot player found: " + whiteName + " vs " + blackName);
		    return;
	    }

	    var botName = isWhiteBot ? whiteName : blackName;
	    var gameId = window.location.pathname.split("/")[1];
	    var gameUrl = MoveStatURL + botName + "/" + gameId + ".json";
	    
	    console.log("Bot player found: " + botName + ", fetching move stats from " + gameUrl);

	    var panelElem = document.createElement("div");
	    panelElem.className="move-stat";
	    panelElem.innerText="Loading move stat...";
	    tabPanel.prepend(panelElem);

	    var tablist = computer.parentElement;
	    var moveStat = document.createElement("button");
	    moveStat.className = ""
	    moveStat.setAttribute("role", "tab");
	    moveStat.setAttribute("data-panel", "move-stat");
	    moveStat.innerText = "Bot Stats";
	    tablist.prepend(moveStat);
	    
	    // Manual tab activation because Lichess code won't know about extra tab.
	    const classMutation = (mutations, observer) => {
		    for (const mutation of mutations) {
			    if (mutation.type === "attributes" && mutation.attributeName === "class") {
				    const panel = document.querySelector("div.move-stat");
				    if (moveStat.className.indexOf("active") !== -1) {
					    panel.classList.add("active");
				    } else {
					    panel.classList.remove("active");
				    }
			    }
		    }
	    }
	    var observer = new MutationObserver(classMutation)
	    observer.observe(moveStat, { attributes: true });

	    var gameData = null;

	    const tableHeader = `
<section class="explorer-box" id="move-stat-panel">
	<table class="moves">
		<thead>
			<tr>
				<th>Move</th>
				<th>Visits</th>
				<th>Policy</th>
				<th>Score (W/D/L)</th>
				<th>Offset (W/D/L)</th>
				<th>PV</th>
			</tr>
		</thead>
		<tbody>`;
	    const tableRowTemplate = (move, visits, policy, score, offset, pv) => `
	    		<tr>
				<td>${move}</td>
				<td>${visits}</td>
				<td>${policy}</td>
				<td>${score}</td>
				<td>${offset}</td>
				<td class="pv-relative">${pv}</td>
			</tr>`;
	    const pvStyle = `
	    section.allow-overflow {
		    overflow: visible;
	    }
	    .explorer-box tr td.pv-relative {
		    position: relative;
	    }
	    .explorer-box tr div.pv_box {
		    position: absolute;
		    top: 1px;
		    bottom: 1px;
	    }`;
	    const pvTemplate = (pv) => `<div class="pv_box"><div class="pv pv--nowrap"><span class="pv-san">${pv}</span></div></div>`;
	    const tableFooter = "</tbody></table></section>";

	    var currentMove = -1;

	    var styleElem = document.createElement("style");
	    styleElem.innerHTML = pvStyle;

	    document.querySelector("head").appendChild(styleElem);

	    const HashChangeHandler = (e) => {
		    const moves = document.querySelector("div.analyse__moves move.active");
		    const moveNumber = moves ? moves.getAttribute("p").length / 2 : 0;
		    const panel = document.querySelector("div.move-stat");
		    if (isNaN(moveNumber) || moveNumber < 0) {
			    panel.innerText = "Invalid move number detected: " + moveNumber;
			    return;
		    }

		    if (moveNumber === currentMove) {
			    return;
		    }
		    console.log("Hash changed: " + window.location.hash + ", move number: " + moveNumber);
		    currentMove = moveNumber;

		    const moveData = gameData[moveNumber.toString()];
		    if (!moveData) {
			    panel.innerText = "No move data found for move number: " + moveNumber;
			    return;
		    }
		    const pvData = gameData[moveNumber.toString() + ".pv"];

		    var tableHTML = tableHeader;
		    for (const moveCandidate of moveData) {
			    const san = moveCandidate.move;
			    const visits = moveCandidate.visits;
			    const policy = moveCandidate.policy.toFixed(2) + "%";
			    const wl = moveCandidate.winlose;
			    const draw = moveCandidate.draw;
			    const offsetData = moveCandidate.offset;

			    var score = "";
			    var offset = "";

			    if (moveCandidate.hasOwnProperty("winlose")) {
				    const w = (1.0 + wl - draw) / 2.0
				    const l = (1.0 - wl - draw) / 2.0
				    score = (w + draw / 2.0) * 100.0;
				    score = score.toFixed(2) + "% (" + (w * 100.0).toFixed(0) + "/" + (draw * 100.0).toFixed(0) + "/" + (l * 100.0).toFixed(0) + ")";
			    }

			    if (moveCandidate.hasOwnProperty("offset")) {
				    offset = (offsetData * 50.0).toFixed(2) + "%";
				    if (moveCandidate.hasOwnProperty("winlose")) {
					    const wlo = wl + offsetData / 2.0;
					    const w = (1.0 + wlo - draw) / 2.0
					    const l = (1.0 - wlo - draw) / 2.0
					    offset += " (" + (w * 100.0).toFixed(0) + "/" + (draw * 100.0).toFixed(0) + "/" + (l * 100.0).toFixed(0) + ")";
				    }
			    }

			    var pv = "";
			    if (pvData) {
				    if (pvData.match("[0-9]+[.]+" + san)) {
					    pv = pvTemplate(pvData);
				    }
			    }

			    tableHTML += tableRowTemplate(san, visits, policy, score, offset, pv);
		    }
		    tableHTML += tableFooter;
		    panel.innerHTML = tableHTML;
		    var pvs = document.querySelectorAll(".pv-relative div.pv_box");

		    for (const pv of pvs) {
			    var p = pv.parentElement;
			    p.addEventListener("mouseover", (e) => {
				    document.getElementById("move-stat-panel").classList.add("allow-overflow");
			    });
			    p.addEventListener("mouseout", (e) => {
				    document.getElementById("move-stat-panel").classList.remove("allow-overflow");
			    });
		    }
	    }

	    const ActivateMoveStatTab = () => {
		    if (!gameData) return;
		    const pageChangeTimeout = 100;
		    const handler = () => {
			    // Activate the first move stat display.
			    HashChangeHandler();
			    setTimeout(handler, pageChangeTimeout);
		    }
		    handler();
	    }

	    fetch(gameUrl).then(response => {
		    const panel = document.querySelector("div.move-stat");
		    if (!response.ok) {
			    if (response.status === 404) {
				    panel.innerText = "No move stats found for this game.";
				    return;
			    }
			    panel.innertText = "Error fetching move stats: " + response.status;
			    throw new Error("Network response: " + response.status);
		    }
		    panel.innerText = "Move stats loaded.";
		    response.json().then(data => {
			    gameData = data;
			    ActivateMoveStatTab();
		    }).catch(err => {
			    const panel = document.querySelector("div.move-stat");
			    panel.innerText = "Error parsing move stats: " + err;
		    });
	    }).catch(err => {
		    const panel = document.querySelector("div.move-stat");
		    panel.innerText = "Error fetching move stats: " + err;
	    });
    }

    console.log("Move stat initialized");
    AddMoveStats();
}();
