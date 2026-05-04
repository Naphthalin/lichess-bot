"""An engine mimics a UCI engine."""

import chess
import typing

assert input() == "uci"

verbose_stats = [
    # Test go nodes 1 where verbose stats are unknown
    "bestmove a2a3",
    """info depth 1 seldepth 1 time 2048 nodes 1 score cp 111 tbhits 0 pv e7e5
info string f7f6  (346 ) N:       0 (+ 0) (P:  0.38%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.00666) (UM: 0.00000) (S:  0.34645) (V:  -.----) 
info string g7g5  (378 ) N:       0 (+ 0) (P:  0.60%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01051) (UM: 0.00000) (S:  0.35029) (V:  -.----) 
info string g8h6  (161 ) N:       0 (+ 0) (P:  0.62%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01080) (UM: 0.00000) (S:  0.35059) (V:  -.----) 
info string b7b5  (234 ) N:       0 (+ 0) (P:  0.64%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01125) (UM: 0.00000) (S:  0.35103) (V:  -.----) 
info string b8a6  (34  ) N:       0 (+ 0) (P:  0.72%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01250) (UM: 0.00000) (S:  0.35228) (V:  -.----) 
info string a7a5  (207 ) N:       0 (+ 0) (P:  0.73%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01276) (UM: 0.00000) (S:  0.35254) (V:  -.----) 
info string h7h5  (403 ) N:       0 (+ 0) (P:  0.74%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01290) (UM: 0.00000) (S:  0.35269) (V:  -.----) 
info string f7f5  (351 ) N:       0 (+ 0) (P:  0.76%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01330) (UM: 0.00000) (S:  0.35309) (V:  -.----) 
info string b7b6  (230 ) N:       0 (+ 0) (P:  0.90%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.01578) (UM: 0.00000) (S:  0.35557) (V:  -.----) 
info string h7h6  (400 ) N:       0 (+ 0) (P:  1.32%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.02296) (UM: 0.00000) (S:  0.36274) (V:  -.----) 
info string b8c6  (36  ) N:       0 (+ 0) (P:  1.40%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.02440) (UM: 0.00000) (S:  0.36419) (V:  -.----) 
info string d7d6  (288 ) N:       0 (+ 0) (P:  2.42%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.04227) (UM: 0.00000) (S:  0.38206) (V:  -.----) 
info string c7c6  (259 ) N:       0 (+ 0) (P:  2.56%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.04468) (UM: 0.00000) (S:  0.38447) (V:  -.----) 
info string a7a6  (204 ) N:       0 (+ 0) (P:  3.34%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.05829) (UM: 0.00000) (S:  0.39807) (V:  -.----) 
info string e7e6  (317 ) N:       0 (+ 0) (P:  4.61%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.08044) (UM: 0.00000) (S:  0.42023) (V:  -.----) 
info string g7g6  (374 ) N:       0 (+ 0) (P:  9.28%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.16195) (UM: 0.00000) (S:  0.50174) (V:  -.----) 
info string d7d5  (293 ) N:       0 (+ 0) (P: 10.44%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.18214) (UM: 0.00000) (S:  0.52192) (V:  -.----) 
info string g8f6  (159 ) N:       0 (+ 0) (P: 11.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.19321) (UM: 0.00000) (S:  0.53300) (V:  -.----) 
info string c7c5  (264 ) N:       0 (+ 0) (P: 23.45%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.40922) (UM: 0.00000) (S:  0.74900) (V:  -.----) 
info string e7e5  (322 ) N:       0 (+ 0) (P: 24.01%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.33978) (U: 0.41902) (UM: 0.00000) (S:  0.75880) (V:  -.----) 
info string node  (  20) N:       1 (+ 0) (P:  0.00%) (WL:  0.33695) (D: 0.297) (M: 130.9) (Q:  0.33695) (V:  0.3398)
bestmove e7e5""",
    # Test go nodes 1 with TempUtilityDevition enabled
    "bestmove a3a4",
    """info depth 1 seldepth 1 time 8699 nodes 1 score cp 301 tbhits 0 pv f8c5
info string f8a3  (143 ) N:       0 (+ 0) (P:  0.24%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00421) (UM: 0.00000) (O: -0.00669) (S:  0.70736) (V:  -.----) 
info string e8e7  (106 ) N:       0 (+ 0) (P:  0.26%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00455) (UM: 0.00000) (O:  0.01352) (S:  0.72790) (V:  -.----) 
info string d8h4  (93  ) N:       0 (+ 0) (P:  0.29%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00507) (UM: 0.00000) (O: -0.00161) (S:  0.71329) (V:  -.----) 
info string e5e4  (796 ) N:       0 (+ 0) (P:  0.31%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00533) (UM: 0.00000) (O: -0.00225) (S:  0.71291) (V:  -.----) 
info string b7b5  (234 ) N:       0 (+ 0) (P:  0.32%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00561) (UM: 0.00000) (O: -0.00616) (S:  0.70928) (V:  -.----) 
info string d8g5  (91  ) N:       0 (+ 0) (P:  0.33%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00573) (UM: 0.00000) (O:  0.02876) (S:  0.74432) (V:  -.----) 
info string g8h6  (161 ) N:       0 (+ 0) (P:  0.33%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00583) (UM: 0.00000) (O:  0.01024) (S:  0.72591) (V:  -.----) 
info string b8a6  (34  ) N:       0 (+ 0) (P:  0.36%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00636) (UM: 0.00000) (O:  0.00259) (S:  0.71878) (V:  -.----) 
info string f8b4  (141 ) N:       0 (+ 0) (P:  0.37%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00641) (UM: 0.00000) (O: -0.00799) (S:  0.70825) (V:  -.----) 
info string d8f6  (88  ) N:       0 (+ 0) (P:  0.37%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00646) (UM: 0.00000) (O: -0.01302) (S:  0.70327) (V:  -.----) 
info string g7g5  (378 ) N:       0 (+ 0) (P:  0.38%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00665) (UM: 0.00000) (O: -0.00997) (S:  0.70651) (V:  -.----) 
info string f8d6  (134 ) N:       0 (+ 0) (P:  0.39%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00675) (UM: 0.00000) (O:  0.01261) (S:  0.72919) (V:  -.----) 
info string f7f6  (346 ) N:       0 (+ 0) (P:  0.39%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00681) (UM: 0.00000) (O:  0.02356) (S:  0.74020) (V:  -.----) 
info string b7b6  (230 ) N:       0 (+ 0) (P:  0.40%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00693) (UM: 0.00000) (O: -0.01121) (S:  0.70555) (V:  -.----) 
info string c7c5  (264 ) N:       0 (+ 0) (P:  0.47%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00824) (UM: 0.00000) (O: -0.00289) (S:  0.71518) (V:  -.----) 
info string d7d5  (139 ) N:       0 (+ 0) (P:  0.50%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.00872) (UM: 0.00000) (O: -0.00886) (S:  0.70970) (V:  -.----) 
info string d8e7  (82  ) N:       0 (+ 0) (P:  0.58%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01017) (UM: 0.00000) (O: -0.00811) (S:  0.71189) (V:  -.----) 
info string c7c6  (259 ) N:       0 (+ 0) (P:  0.58%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01018) (UM: 0.00000) (O:  0.01787) (S:  0.73789) (V:  -.----) 
info string d7d6  (288 ) N:       0 (+ 0) (P:  0.67%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01169) (UM: 0.00000) (O:  0.00637) (S:  0.72789) (V:  -.----) 
info string g7g6  (374 ) N:       0 (+ 0) (P:  0.69%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01204) (UM: 0.00000) (O: -0.01907) (S:  0.70280) (V:  -.----) 
info string h7h5  (403 ) N:       0 (+ 0) (P:  0.70%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01218) (UM: 0.00000) (O:  0.00958) (S:  0.73159) (V:  -.----) 
info string f7f5  (351 ) N:       0 (+ 0) (P:  0.74%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01285) (UM: 0.00000) (O:  0.00422) (S:  0.72691) (V:  -.----) 
info string a7a5  (207 ) N:       0 (+ 0) (P:  0.85%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01488) (UM: 0.00000) (O:  0.00645) (S:  0.73116) (V:  -.----) 
info string h7h6  (400 ) N:       0 (+ 0) (P:  0.85%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.01488) (UM: 0.00000) (O:  0.01272) (S:  0.73743) (V:  -.----) 
info string f8e7  (130 ) N:       0 (+ 0) (P:  1.55%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.02697) (UM: 0.00000) (O: -0.00488) (S:  0.73192) (V:  -.----) 
info string g8e7  (154 ) N:       0 (+ 0) (P:  2.00%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.03496) (UM: 0.00000) (O: -0.00711) (S:  0.73768) (V:  -.----) 
info string a7a6  (204 ) N:       0 (+ 0) (P:  3.25%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.05674) (UM: 0.00000) (O: -0.00621) (S:  0.76037) (V:  -.----) 
info string g8f6  (159 ) N:       0 (+ 0) (P:  8.37%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.14614) (UM: 0.00000) (O: -0.02150) (S:  0.83447) (V:  -.----) 
info string b8c6  (36  ) N:       0 (+ 0) (P: 27.76%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.48442) (UM: 0.00000) (O:  0.00743) (S:  1.20168) (V:  -.----) 
info string f8c5  (293 ) N:       0 (+ 0) (P: 45.69%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.70983) (U: 0.79735) (UM: 0.00000) (O:  0.00948) (S:  1.51667) (V:  -.----) 
info string node  (  30) N:       1 (+ 0) (P:  0.00%) (WL:  0.71149) (D: 0.145) (M: 89.8) (Q:  0.71149) (V:  0.7098) 
bestmove f8c5""",
    # Test go nodes 1000 with MultiPV 5
    "bestmove a4a5",
    """info depth 1 seldepth 1 time 25534 nodes 2 score cp -552 nps 222 tbhits 0 multipv 1 pv d7d5 e2e3
info depth 1 seldepth 1 time 25534 nodes 2 score cp -72 nps 222 tbhits 0 multipv 2 pv b8c6
info depth 1 seldepth 1 time 25534 nodes 2 score cp -72 nps 222 tbhits 0 multipv 3 pv a7a6
info depth 1 seldepth 1 time 25534 nodes 2 score cp -72 nps 222 tbhits 0 multipv 4 pv g8f6
info depth 1 seldepth 1 time 25534 nodes 2 score cp -72 nps 222 tbhits 0 multipv 5 pv g8e7
info depth 1 seldepth 1 time 25543 nodes 5 score cp -469 nps 277 tbhits 0 multipv 1 pv a7a6 e2e3
info depth 1 seldepth 1 time 25543 nodes 5 score cp -475 nps 277 tbhits 0 multipv 2 pv g8f6 e2e3
info depth 1 seldepth 1 time 25543 nodes 5 score cp -552 nps 277 tbhits 0 multipv 3 pv d7d5 e2e3
info depth 1 seldepth 1 time 25543 nodes 5 score cp -653 nps 277 tbhits 0 multipv 4 pv b8c6 c2c3
info depth 1 seldepth 1 time 25543 nodes 5 score cp -711 nps 277 tbhits 0 multipv 5 pv g8e7
info depth 1 seldepth 2 time 25550 nodes 6 score cp -106 nps 250 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6
info depth 1 seldepth 2 time 25550 nodes 6 score cp -475 nps 250 tbhits 0 multipv 2 pv g8f6 e2e3
info depth 1 seldepth 2 time 25550 nodes 6 score cp -552 nps 250 tbhits 0 multipv 3 pv d7d5 e2e3
info depth 1 seldepth 2 time 25550 nodes 6 score cp -653 nps 250 tbhits 0 multipv 4 pv b8c6 c2c3
info depth 1 seldepth 2 time 25550 nodes 6 score cp -469 nps 250 tbhits 0 multipv 5 pv g8e7
info depth 1 seldepth 2 time 25556 nodes 11 score cp 255 nps 354 tbhits 0 multipv 1 pv d7d5 e2e3 b8c6
info depth 1 seldepth 2 time 25556 nodes 11 score cp 142 nps 354 tbhits 0 multipv 2 pv a7a6 e2e3 b8c6
info depth 1 seldepth 2 time 25556 nodes 11 score cp -59 nps 354 tbhits 0 multipv 3 pv g8f6 e2e3 b8c6
info depth 1 seldepth 2 time 25556 nodes 11 score cp -135 nps 354 tbhits 0 multipv 4 pv b8c6 c2c3 a7a6
info depth 1 seldepth 2 time 25556 nodes 11 score cp 174 nps 354 tbhits 0 multipv 5 pv g8e7
info depth 1 seldepth 3 time 25563 nodes 14 score cp 267 nps 378 tbhits 0 multipv 1 pv d7d5 e2e3 b8c6 a5a6
info depth 1 seldepth 3 time 25563 nodes 14 score cp 142 nps 378 tbhits 0 multipv 2 pv a7a6 e2e3 b8c6
info depth 1 seldepth 3 time 25563 nodes 14 score cp -59 nps 378 tbhits 0 multipv 3 pv g8f6 e2e3 b8c6
info depth 1 seldepth 3 time 25563 nodes 14 score cp -135 nps 378 tbhits 0 multipv 4 pv b8c6 c2c3 a7a6
info depth 1 seldepth 3 time 25563 nodes 14 score cp 193 nps 378 tbhits 0 multipv 5 pv g8e7
info depth 2 seldepth 3 time 25569 nodes 23 score cp -531 nps 522 tbhits 0 multipv 1 pv d7d5 g2g3 b8c6 f1g2
info depth 2 seldepth 3 time 25569 nodes 23 score cp 406 nps 522 tbhits 0 multipv 2 pv b8c6 a5a6 b7a6
info depth 2 seldepth 3 time 25569 nodes 23 score cp 16 nps 522 tbhits 0 multipv 3 pv a7a6 e2e3 b8c6 c2c3
info depth 2 seldepth 3 time 25569 nodes 23 score cp -59 nps 522 tbhits 0 multipv 4 pv g8f6 e2e3 b8c6
info depth 2 seldepth 3 time 25569 nodes 23 score cp -3 nps 522 tbhits 0 multipv 5 pv g8e7
info depth 2 seldepth 3 time 25578 nodes 30 score cp -475 nps 566 tbhits 0 multipv 1 pv b8c6 a5a6 b7a6 e2e3
info depth 2 seldepth 3 time 25578 nodes 30 score cp -531 nps 566 tbhits 0 multipv 2 pv d7d5 g2g3 b8c6 f1g2
info depth 2 seldepth 3 time 25578 nodes 30 score cp 16 nps 566 tbhits 0 multipv 3 pv a7a6 e2e3 b8c6 c2c3
info depth 2 seldepth 3 time 25578 nodes 30 score cp -59 nps 566 tbhits 0 multipv 4 pv g8f6 e2e3 b8c6
info depth 2 seldepth 3 time 25578 nodes 30 score cp -255 nps 566 tbhits 0 multipv 5 pv g8e7
info depth 2 seldepth 4 time 25606 nodes 40 score cp -475 nps 493 tbhits 0 multipv 1 pv b8c6 a5a6 b7a6 e2e3
info depth 2 seldepth 4 time 25606 nodes 40 score cp -531 nps 493 tbhits 0 multipv 2 pv d7d5 g2g3 b8c6 f1g2
info depth 2 seldepth 4 time 25606 nodes 40 score cp 100 nps 493 tbhits 0 multipv 3 pv a7a6 e2e3 b8c6 g2g3 d7d5
info depth 2 seldepth 4 time 25606 nodes 40 score cp -111 nps 493 tbhits 0 multipv 4 pv g8f6 e2e3 d7d5 d2d4
info depth 2 seldepth 4 time 25606 nodes 40 score cp -175 nps 493 tbhits 0 multipv 5 pv g8e7
info depth 2 seldepth 5 time 25606 nodes 42 score cp -475 nps 518 tbhits 0 multipv 1 pv b8c6 a5a6 b7a6 e2e3
info depth 2 seldepth 5 time 25606 nodes 42 score cp 67 nps 518 tbhits 0 multipv 2 pv a7a6 e2e3 b8c6 c2c3 c5a7 d2d4
info depth 2 seldepth 5 time 25606 nodes 42 score cp -531 nps 518 tbhits 0 multipv 3 pv d7d5 g2g3 b8c6 f1g2
info depth 2 seldepth 5 time 25606 nodes 42 score cp -111 nps 518 tbhits 0 multipv 4 pv g8f6 e2e3 d7d5 d2d4
info depth 2 seldepth 5 time 25606 nodes 42 score cp -175 nps 518 tbhits 0 multipv 5 pv g8e7
info depth 2 seldepth 5 time 25616 nodes 44 score cp 34 nps 488 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d4
info depth 2 seldepth 5 time 25616 nodes 44 score cp -475 nps 488 tbhits 0 multipv 2 pv b8c6 a5a6 b7a6 e2e3
info depth 2 seldepth 5 time 25616 nodes 44 score cp -531 nps 488 tbhits 0 multipv 3 pv d7d5 g2g3 b8c6 f1g2
info depth 2 seldepth 5 time 25616 nodes 44 score cp -111 nps 488 tbhits 0 multipv 4 pv g8f6 e2e3 d7d5 d2d4
info depth 2 seldepth 5 time 25616 nodes 44 score cp -176 nps 488 tbhits 0 multipv 5 pv g8e7
info depth 2 seldepth 6 time 25629 nodes 51 score cp -70 nps 495 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d4 c5d6
info depth 2 seldepth 6 time 25629 nodes 51 score cp 301 nps 495 tbhits 0 multipv 2 pv g8f6 e2e3 b8c6 c2c3 d7d5
info depth 2 seldepth 6 time 25629 nodes 51 score cp -475 nps 495 tbhits 0 multipv 3 pv b8c6 a5a6 b7a6 e2e3
info depth 2 seldepth 6 time 25629 nodes 51 score cp -531 nps 495 tbhits 0 multipv 4 pv d7d5 g2g3 b8c6 f1g2
info depth 2 seldepth 6 time 25629 nodes 51 score cp -105 nps 495 tbhits 0 multipv 5 pv g8e7
info depth 3 seldepth 6 time 25638 nodes 56 score cp -168 nps 495 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d4 c5d6
info depth 3 seldepth 6 time 25638 nodes 56 score cp 61 nps 495 tbhits 0 multipv 2 pv g8f6 e2e3 b8c6 c2c3 d7d5 d2d4
info depth 3 seldepth 6 time 25638 nodes 56 score cp -475 nps 495 tbhits 0 multipv 3 pv b8c6 a5a6 b7a6 e2e3
info depth 3 seldepth 6 time 25638 nodes 56 score cp -531 nps 495 tbhits 0 multipv 4 pv d7d5 g2g3 b8c6 f1g2
info depth 3 seldepth 6 time 25638 nodes 56 score cp -196 nps 495 tbhits 0 multipv 5 pv g8e7
info depth 3 seldepth 7 time 25662 nodes 75 score cp -43 nps 551 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d3 g8f6
info depth 3 seldepth 7 time 25662 nodes 75 score cp -278 nps 551 tbhits 0 multipv 2 pv g8f6 e2e3 b8c6 c2c3 d7d5 d2d4 c5d6
info depth 3 seldepth 7 time 25662 nodes 75 score cp -440 nps 551 tbhits 0 multipv 3 pv b8c6 c2c3 a7a6 e2e3 d7d5
info depth 3 seldepth 7 time 25662 nodes 75 score cp -701 nps 551 tbhits 0 multipv 4 pv d7d5 e2e3 b8c6 a5a6
info depth 3 seldepth 7 time 25662 nodes 75 score cp -200 nps 551 tbhits 0 multipv 5 pv g8e7
info depth 3 seldepth 8 time 25688 nodes 118 score cp -158 nps 723 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d4 c5d6 g2g3 g8f6
info depth 3 seldepth 8 time 25688 nodes 118 score cp -382 nps 723 tbhits 0 multipv 2 pv g8f6 e2e3 b8c6 c2c3 d7d5 a5a6 e8g8 d2d4
info depth 3 seldepth 8 time 25688 nodes 118 score cp -310 nps 723 tbhits 0 multipv 3 pv d7d5 g2g3 b8c6 c2c3 a7a6
info depth 3 seldepth 8 time 25688 nodes 118 score cp -673 nps 723 tbhits 0 multipv 4 pv b8c6 a5a6 g8f6 e2e3
info depth 3 seldepth 8 time 25688 nodes 118 score cp -297 nps 723 tbhits 0 multipv 5 pv g8e7
info depth 4 seldepth 8 time 25696 nodes 132 score cp -201 nps 776 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d4 c5d6 g2g3 g8f6
info depth 4 seldepth 8 time 25696 nodes 132 score cp -148 nps 776 tbhits 0 multipv 2 pv d7d5 c2c3 b8c6 a5a6 g8f6
info depth 4 seldepth 8 time 25696 nodes 132 score cp -489 nps 776 tbhits 0 multipv 3 pv g8f6 e2e3 b8c6 c2c3 d7d5 a5a6 e8g8 d2d4
info depth 4 seldepth 8 time 25696 nodes 132 score cp -563 nps 776 tbhits 0 multipv 4 pv b8c6 a5a6 b7a6 e2e3 g8f6
info depth 4 seldepth 8 time 25696 nodes 132 score cp -276 nps 776 tbhits 0 multipv 5 pv g8e7
info depth 4 seldepth 9 time 25712 nodes 159 score cp -187 nps 850 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d3 g8f6 g2g3 e8g8 f1g2
info depth 4 seldepth 9 time 25712 nodes 159 score cp -273 nps 850 tbhits 0 multipv 2 pv d7d5 c2c3 b8c6 a5a6 g8f6 e2e3
info depth 4 seldepth 9 time 25712 nodes 159 score cp -489 nps 850 tbhits 0 multipv 3 pv g8f6 e2e3 b8c6 c2c3 d7d5 a5a6 e8g8 d2d4
info depth 4 seldepth 9 time 25712 nodes 159 score cp -465 nps 850 tbhits 0 multipv 4 pv b8c6 a5a6 b7a6 e2e3 g8f6
info depth 4 seldepth 9 time 25712 nodes 159 score cp -278 nps 850 tbhits 0 multipv 5 pv g8e7
info depth 4 seldepth 9 time 25759 nodes 238 score cp -189 nps 1017 tbhits 0 multipv 1 pv d7d5 e2e3 b8c6 a5a6 g8f6 a6b7 c8b7 d2d3 e8g8
info depth 4 seldepth 9 time 25759 nodes 238 score cp -243 nps 1017 tbhits 0 multipv 2 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d3 g8f6 g2g3 e8g8 f1g2
info depth 4 seldepth 9 time 25759 nodes 238 score cp -495 nps 1017 tbhits 0 multipv 3 pv b8c6 a5a6 b7a6 e2e3 a6a5 f1b5
info depth 4 seldepth 9 time 25759 nodes 238 score cp -489 nps 1017 tbhits 0 multipv 4 pv g8f6 e2e3 b8c6 c2c3 d7d5 a5a6 e8g8 d2d4
info depth 4 seldepth 9 time 25759 nodes 238 score cp -273 nps 1017 tbhits 0 multipv 5 pv g8e7
info depth 4 seldepth 9 time 25806 nodes 298 score cp -272 nps 1060 tbhits 0 multipv 1 pv a7a6 e2e3 b8c6 c2c3 d7d5 d2d3 g8f6 g2g3 e8g8 f1g2
info depth 4 seldepth 9 time 25806 nodes 298 score cp -264 nps 1060 tbhits 0 multipv 2 pv d7d5 e2e3 b8c6 a5a6 g8f6 c2c3 e8g8 d2d4 c5d6
info depth 4 seldepth 9 time 25806 nodes 298 score cp -525 nps 1060 tbhits 0 multipv 3 pv b8c6 a5a6 b7a6 e2e3 a6a5 f1b5
info depth 4 seldepth 9 time 25806 nodes 298 score cp -440 nps 1060 tbhits 0 multipv 4 pv g8f6 e2e3 b8c6 c2c3 d7d5 a5a6 e8g8 d2d4
info depth 4 seldepth 9 time 25806 nodes 298 score cp -802 nps 1060 tbhits 0 multipv 5 pv g8e7 c2c3
info depth 5 seldepth 9 time 25834 nodes 340 score cp -224 nps 1103 tbhits 0 multipv 1 pv a7a6 g2g3 d7d5 f1g2 b8c6 c2c3 g8f6 d2d3
info depth 5 seldepth 9 time 25834 nodes 340 score cp -303 nps 1103 tbhits 0 multipv 2 pv d7d5 e2e3 b8c6 a5a6 g8f6 c2c3 e8g8 d2d4 c5d6
info depth 5 seldepth 9 time 25834 nodes 340 score cp -432 nps 1103 tbhits 0 multipv 3 pv b8c6 a5a6 b7a6 e2e3 g8f6 f1a6 c8a6
info depth 5 seldepth 9 time 25834 nodes 340 score cp -454 nps 1103 tbhits 0 multipv 4 pv g8f6 e2e3 b8c6 a5a6 e8g8 c2c3 d7d5 d2d4
info depth 5 seldepth 9 time 25834 nodes 340 score cp -650 nps 1103 tbhits 0 multipv 5 pv d8e7 c2c3
info depth 5 seldepth 10 time 25870 nodes 416 score cp -338 nps 1205 tbhits 0 multipv 1 pv a7a6 g2g3 h7h5 h2h4 b8c6 c2c3 g8f6 f1g2
info depth 5 seldepth 10 time 25870 nodes 416 score cp -324 nps 1205 tbhits 0 multipv 2 pv d7d5 e2e3 b8c6 a5a6 g8f6 c2c3 e8g8 d2d4 c5d6
info depth 5 seldepth 10 time 25870 nodes 416 score cp -462 nps 1205 tbhits 0 multipv 3 pv g8f6 e2e3 b8c6 a5a6 e8g8 c2c3 d7d5 d2d4 c5d6 f1e2
info depth 5 seldepth 10 time 25870 nodes 416 score cp -501 nps 1205 tbhits 0 multipv 4 pv b8c6 a5a6 b7a6 e2e3 g8f6 f1a6 c8a6
info depth 5 seldepth 10 time 25870 nodes 416 score cp -634 nps 1205 tbhits 0 multipv 5 pv c7c6 e2e3
info depth 5 seldepth 10 time 26072 nodes 704 score cp -269 nps 1287 tbhits 0 multipv 1 pv g8f6 e2e3 b8c6 a5a6 e8g8 c2c3 d7d5 d2d4 c5d6 f1e2
info depth 5 seldepth 10 time 26072 nodes 704 score cp -402 nps 1287 tbhits 0 multipv 2 pv a7a6 g2g3 d7d5 f1g2 b8c6 c2c3 c5a7 d2d3 c8e6 g1f3
info depth 5 seldepth 10 time 26072 nodes 704 score cp -429 nps 1287 tbhits 0 multipv 3 pv d7d5 c2c3 b8c6 a5a6 g8f6 e2e3 e8g8 d2d4 c5d6 a6b7 c8b7
info depth 5 seldepth 10 time 26072 nodes 704 score cp -502 nps 1287 tbhits 0 multipv 4 pv b8c6 a5a6 g8f6 e2e3 e8g8 c2c3 d7d5 d2d4 c5d6
info depth 5 seldepth 10 time 26072 nodes 704 score cp -634 nps 1287 tbhits 0 multipv 5 pv c7c6 e2e3
info depth 5 seldepth 10 time 26112 nodes 802 score cp -351 nps 1366 tbhits 0 multipv 1 pv a7a6 g2g3 b8c6 f1g2 d7d5 c2c3 c5a7 d2d3 g8f6 e2e3 c8g4
info depth 5 seldepth 10 time 26112 nodes 802 score cp -369 nps 1366 tbhits 0 multipv 2 pv g8f6 e2e3 b8c6 a5a6 e8g8 c2c3 d7d5 d2d4 c5d6 f1e2
info depth 5 seldepth 10 time 26112 nodes 802 score cp -424 nps 1366 tbhits 0 multipv 3 pv d7d5 c2c3 b8c6 a5a6 g8f6 e2e3 e8g8 d2d4 c5d6 a6b7 c8b7
info depth 5 seldepth 10 time 26112 nodes 802 score cp -502 nps 1366 tbhits 0 multipv 4 pv b8c6 a5a6 g8f6 e2e3 e8g8 c2c3 d7d5 d2d4 c5d6
info depth 5 seldepth 10 time 26112 nodes 802 score cp -634 nps 1366 tbhits 0 multipv 5 pv c7c6 e2e3
info depth 5 seldepth 10 time 26134 nodes 935 score cp -408 nps 1535 tbhits 0 multipv 1 pv d8h4 g2g3 b8c6 f1g2 d7d5 c2c3 c5b6 d2d3 g8f6 e2e3 c8g4
info depth 5 seldepth 10 time 26134 nodes 935 score cp -376 nps 1535 tbhits 0 multipv 2 pv g8f6 d2d3 d7d5 g2g3 b8c6 a5a6 b7b5 f1g2
info depth 5 seldepth 10 time 26134 nodes 935 score cp -446 nps 1535 tbhits 0 multipv 3 pv d7d5 c2c3 b8c6 a5a6 g8f6 e2e3 e8g8 d2d4 c5d6 a6b7 c8b7
info depth 5 seldepth 10 time 26134 nodes 935 score cp -502 nps 1535 tbhits 0 multipv 4 pv b8c6 a5a6 g8f6 e2e3 e8g8 c2c3 d7d5 d2d4 c5d6
info depth 5 seldepth 10 time 26134 nodes 935 score cp -634 nps 1535 tbhits 0 multipv 5 pv c7c6 e2e3
info string c5e3  (734 ) N:       0 (+ 0) (P:  0.10%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.05484) (UM: 0.00000) (S: -0.61240) (V: -0.9854) 
info string c5a3  (730 ) N:       0 (+ 0) (P:  0.10%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.05591) (UM: 0.00000) (S: -0.61133) (V: -0.9825) 
info string c5b6  (714 ) N:       0 (+ 0) (P:  0.13%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.07201) (UM: 0.00000) (S: -0.59523) (V: -0.9950) 
info string e8e7  (106 ) N:       0 (+ 0) (P:  0.13%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.07460) (UM: 0.00000) (S: -0.59264) (V: -0.9729) 
info string b8a6  (34  ) N:       0 (+ 0) (P:  0.14%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.08013) (UM: 0.00000) (S: -0.58711) (V: -0.9706) 
info string f7f6  (346 ) N:       0 (+ 0) (P:  0.15%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.08274) (UM: 0.00000) (S: -0.58450) (V: -0.9733) 
info string c5b4  (726 ) N:       0 (+ 0) (P:  0.17%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.09673) (UM: 0.00000) (S: -0.57051) (V: -0.9699) 
info string c5d4  (728 ) N:       0 (+ 0) (P:  0.19%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.10661) (UM: 0.00000) (S: -0.56063) (V: -0.9803) 
info string d8g5  (91  ) N:       0 (+ 0) (P:  0.21%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.11588) (UM: 0.00000) (S: -0.55136) (V: -0.9948) 
info string c5d6  (716 ) N:       0 (+ 0) (P:  0.22%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.12410) (UM: 0.00000) (S: -0.54314) (V: -0.9648) 
info string g7g5  (378 ) N:       0 (+ 0) (P:  0.22%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.12426) (UM: 0.00000) (S: -0.54298) (V: -0.9680) 
info string e8f8  (101 ) N:       0 (+ 0) (P:  0.23%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.12661) (UM: 0.00000) (S: -0.54063) (V: -0.9646) 
info string g7g6  (374 ) N:       0 (+ 0) (P:  0.24%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.13558) (UM: 0.00000) (S: -0.53166) (V: -0.9627) 
info string e5e4  (796 ) N:       0 (+ 0) (P:  0.26%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.14589) (UM: 0.00000) (S: -0.52135) (V: -0.9629) 
info string c5f8  (707 ) N:       0 (+ 0) (P:  0.27%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.15021) (UM: 0.00000) (S: -0.51703) (V: -0.8339) 
info string g8h6  (161 ) N:       0 (+ 0) (P:  0.28%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.15673) (UM: 0.00000) (S: -0.51051) (V: -0.9725) 
info string c5f2  (736 ) N:       0 (+ 0) (P:  0.35%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.19726) (UM: 0.00000) (S: -0.46998) (V: -0.9927) 
info string c5e7  (712 ) N:       0 (+ 0) (P:  0.35%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.19753) (UM: 0.00000) (S: -0.46971) (V: -0.9382) 
info string f7f5  (351 ) N:       0 (+ 0) (P:  0.39%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.21616) (UM: 0.00000) (S: -0.45108) (V: -0.9745) 
info string b7b5  (234 ) N:       0 (+ 0) (P:  0.42%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.23603) (UM: 0.00000) (S: -0.43121) (V: -0.9759) 
info string h7h5  (403 ) N:       0 (+ 0) (P:  0.43%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.24211) (UM: 0.00000) (S: -0.42513) (V: -0.9643) 
info string b7b6  (230 ) N:       0 (+ 0) (P:  0.44%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.24735) (UM: 0.00000) (S: -0.41989) (V: -0.9690) 
info string h7h6  (400 ) N:       0 (+ 0) (P:  0.53%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.29423) (UM: 0.00000) (S: -0.37301) (V: -0.9519) 
info string c7c6  (93  ) N:       0 (+ 0) (P:  0.54%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.30288) (UM: 0.00000) (S: -0.36436) (V: -0.9855) 
info string d7d6  (288 ) N:       0 (+ 0) (P:  0.86%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.48017) (UM: 0.00000) (S: -0.18707) (V: -0.9648) 
info string c7c6  (259 ) N:       1 (+ 0) (P:  1.13%) (WL: -0.94245) (D: 0.029) (M: 73.2) (Q: -0.94245) (U: 0.31549) (UM: 0.00000) (S: -0.62710) (V: -0.9426) 
info string d8e7  (82  ) N:       1 (+ 0) (P:  1.28%) (WL: -0.95719) (D: 0.023) (M: 71.4) (Q: -0.95719) (U: 0.35842) (UM: 0.00000) (S: -0.59850) (V: -0.9569) 
info string d8f6  (88  ) N:       1 (+ 0) (P:  1.36%) (WL: -0.96953) (D: 0.015) (M: 52.6) (Q: -0.96953) (U: 0.38095) (UM: 0.00000) (S: -0.58863) (V: -0.9696) 
info string g8e7  (154 ) N:       1 (+ 0) (P:  1.58%) (WL: -0.96652) (D: 0.018) (M: 66.7) (Q: -0.96652) (U: 0.44300) (UM: 0.00000) (S: -0.52367) (V: -0.9667) 
info string b8c6  (36  ) N:      96 (+ 0) (P: 24.51%) (WL: -0.40711) (D: 0.072) (M: 70.9) (Q: -0.40711) (U: 0.14146) (UM: 0.00000) (S: -0.26583) (V: -0.9429) 
info string d7d5  (293 ) N:     175 (+ 0) (P: 24.99%) (WL: -0.36477) (D: 0.074) (M: 71.2) (Q: -0.36477) (U: 0.07950) (UM: 0.00000) (S: -0.28478) (V: -0.9049) 
info string g8f6  (159 ) N:     295 (+ 6) (P: 14.43%) (WL: -0.32473) (D: 0.079) (M: 75.0) (Q: -0.32473) (U: 0.02676) (UM: 0.00000) (S: -0.29787) (V: -0.8576) 
info string d8h4  (204 ) N:     364 (+ 6) (P: 23.36%) (WL: -0.34447) (D: 0.077) (M: 72.0) (Q: -0.34447) (U: 0.03526) (UM: 0.00000) (S: -0.30881) (V: -0.8447) 
info string node  (  33) N:     935 (+12) (P: 92.64%) (WL: -0.35006) (D: 0.076) (M: 73.7) (Q: -0.35006) (V:  0.8073) 
info string Best: d8h4
info string a1a3  (10  ) N:       0 (+ 0) (P:  0.42%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.14404) (UM: 0.00000) (S:  0.17193) (V:  -.----) 
info string a1a2  (7   ) N:       0 (+ 0) (P:  0.49%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.16725) (UM: 0.00000) (S:  0.19514) (V:  -.----) 
info string g2g4  (378 ) N:       0 (+ 0) (P:  0.54%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.18199) (UM: 0.00000) (S:  0.20988) (V:  -.----) 
info string g1h3  (161 ) N:       0 (+ 0) (P:  0.62%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.20876) (UM: 0.00000) (S:  0.23664) (V:  -.----) 
info string b1a3  (34  ) N:       0 (+ 0) (P:  0.67%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.22699) (UM: 0.00000) (S:  0.25488) (V:  -.----) 
info string d2d4  (293 ) N:       0 (+ 0) (P:  0.86%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.29002) (UM: 0.00000) (S:  0.31791) (V:  -.----) 
info string a1a4  (13  ) N:       0 (+ 0) (P:  0.94%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.31950) (UM: 0.00000) (S:  0.34739) (V: -0.5825) 
info string b2b4  (234 ) N:       0 (+ 0) (P:  1.03%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.34976) (UM: 0.00000) (S:  0.37765) (V: -0.8647) 
info string b2b3  (230 ) N:       0 (+ 0) (P:  1.11%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.37756) (UM: 0.00000) (S:  0.40545) (V: -0.7714) 
info string e2e4  (322 ) N:       1 (+ 0) (P:  2.31%) (WL: -0.84514) (D: 0.061) (M: 58.6) (Q: -0.84514) (U: 0.39153) (UM: 0.00000) (S: -0.45425) (V: -0.8458) 
info string b1c3  (36  ) N:       1 (+ 0) (P:  1.74%) (WL: -0.69201) (D: 0.111) (M: 77.0) (Q: -0.69201) (U: 0.29442) (UM: 0.00000) (S: -0.39739) (V: -0.6918) 
info string h2h3  (400 ) N:       1 (+ 0) (P:  1.37%) (WL: -0.52070) (D: 0.158) (M: 87.3) (Q: -0.52070) (U: 0.23255) (UM: 0.00000) (S: -0.29013) (V: -0.5227) 
info string c2c4  (264 ) N:       1 (+ 0) (P:  1.94%) (WL: -0.41494) (D: 0.152) (M: 85.4) (Q: -0.41494) (U: 0.32881) (UM: 0.00000) (S: -0.08302) (V: -0.4118) 
info string g1f3  (159 ) N:       1 (+ 0) (P:  4.19%) (WL: -0.54600) (D: 0.135) (M: 83.1) (Q: -0.54600) (U: 0.71012) (UM: 0.00000) (S:  0.16206) (V: -0.5481) 
info string d2d3  (288 ) N:      13 (+ 0) (P:  8.90%) (WL: -0.09678) (D: 0.108) (M: 81.8) (Q: -0.09678) (U: 0.21545) (UM: 0.00000) (S:  0.12004) (V: -0.7218) 
info string c2c3  (259 ) N:      22 (+ 0) (P: 28.66%) (WL:  0.01356) (D: 0.088) (M: 76.7) (Q:  0.01356) (U: 0.42240) (UM: 0.00000) (S:  0.43575) (V: -0.6667) 
info string e2e3  (317 ) N:      50 (+ 0) (P: 29.43%) (WL:  0.16068) (D: 0.089) (M: 75.4) (Q:  0.16068) (U: 0.19561) (UM: 0.00000) (S:  0.35655) (V: -0.6404) 
info string g2g3  (374 ) N:     273 (+ 6) (P: 13.26%) (WL:  0.44033) (D: 0.078) (M: 69.0) (Q:  0.44033) (U: 0.01606) (UM: 0.00000) (S:  0.45678) (V: -0.5258) 
info string node  (  21) N:     364 (+ 6) (P: 91.80%) (WL:  0.34447) (D: 0.077) (M: 72.0) (Q:  0.34447) (V:  0.8447) 
bestmove d8h4 ponder g2g3""",
    "bestmove a5a6",
    """info depth 1 seldepth 1 time 6891 nodes 233 score mate 1 nps 58250 tbhits 0 multipv 1 pv c5f2
info depth 1 seldepth 1 time 6891 nodes 233 score mate 1 nps 58250 tbhits 0 multipv 2 pv h4f2
info depth 1 seldepth 1 time 6891 nodes 233 score cp 12796 nps 58250 tbhits 0 multipv 3 pv b8a6
info depth 1 seldepth 1 time 6891 nodes 233 score cp 12796 nps 58250 tbhits 0 multipv 4 pv b7a6
info depth 1 seldepth 1 time 6891 nodes 233 score cp 12796 nps 58250 tbhits 0 multipv 5 pv b7b6
info string g8e7  (154 ) N:       0 (+ 0) (P:  0.04%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01033) (UM: 0.00000) (S:  0.69108) (V:  -.----) 
info string h4g5  (1123) N:       0 (+ 0) (P:  0.04%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01102) (UM: 0.00000) (S:  0.69177) (V:  -.----) 
info string f7f6  (346 ) N:       0 (+ 0) (P:  0.04%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01141) (UM: 0.00000) (S:  0.69216) (V:  -.----) 
info string h4d8  (1115) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01220) (UM: 0.00000) (S:  0.69295) (V:  -.----) 
info string g8h6  (161 ) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01231) (UM: 0.00000) (S:  0.69306) (V:  -.----) 
info string h4g3  (1133) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01256) (UM: 0.00000) (S:  0.69331) (V:  -.----) 
info string h4h2  (1137) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01260) (UM: 0.00000) (S:  0.69335) (V:  -.----) 
info string c7c6  (259 ) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01315) (UM: 0.00000) (S:  0.69390) (V:  -.----) 
info string h4g4  (1131) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01369) (UM: 0.00000) (S:  0.69444) (V:  -.----) 
info string h4h6  (1121) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01389) (UM: 0.00000) (S:  0.69464) (V:  -.----) 
info string h4h5  (1124) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01401) (UM: 0.00000) (S:  0.69476) (V:  -.----) 
info string b8c6  (36  ) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01449) (UM: 0.00000) (S:  0.69524) (V:  -.----) 
info string h4e7  (1117) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01449) (UM: 0.00000) (S:  0.69524) (V:  -.----) 
info string h4f4  (1130) N:       0 (+ 0) (P:  0.05%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01478) (UM: 0.00000) (S:  0.69553) (V:  -.----) 
info string e8d8  (100 ) N:       0 (+ 0) (P:  0.06%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01546) (UM: 0.00000) (S:  0.69621) (V:  -.----) 
info string e8f8  (101 ) N:       0 (+ 0) (P:  0.06%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01546) (UM: 0.00000) (S:  0.69621) (V:  -.----) 
info string h4h3  (1134) N:       0 (+ 0) (P:  0.06%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01616) (UM: 0.00000) (S:  0.69690) (V:  -.----) 
info string e8e7  (106 ) N:       0 (+ 0) (P:  0.06%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01690) (UM: 0.00000) (S:  0.69765) (V:  -.----) 
info string h4c4  (1127) N:       0 (+ 0) (P:  0.06%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01705) (UM: 0.00000) (S:  0.69780) (V:  -.----) 
info string h4f6  (1119) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01759) (UM: 0.00000) (S:  0.69834) (V:  -.----) 
info string f7f5  (351 ) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01764) (UM: 0.00000) (S:  0.69839) (V:  -.----) 
info string c5b6  (714 ) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01816) (UM: 0.00000) (S:  0.69891) (V:  -.----) 
info string g8f6  (159 ) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01832) (UM: 0.00000) (S:  0.69907) (V:  -.----) 
info string h4d4  (1128) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01837) (UM: 0.00000) (S:  0.69912) (V:  -.----) 
info string c5e3  (734 ) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01908) (UM: 0.00000) (S:  0.69983) (V:  -.----) 
info string h4b4  (1126) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01913) (UM: 0.00000) (S:  0.69988) (V:  -.----) 
info string d7d6  (288 ) N:       0 (+ 0) (P:  0.07%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.01947) (UM: 0.00000) (S:  0.70022) (V:  -.----) 
info string b7b5  (234 ) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02035) (UM: 0.00000) (S:  0.70109) (V:  -.----) 
info string h4a4  (1125) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02071) (UM: 0.00000) (S:  0.70145) (V:  -.----) 
info string g7g5  (378 ) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02096) (UM: 0.00000) (S:  0.70170) (V:  -.----) 
info string c5d6  (716 ) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02096) (UM: 0.00000) (S:  0.70170) (V:  -.----) 
info string g7g6  (374 ) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02120) (UM: 0.00000) (S:  0.70195) (V:  -.----) 
info string e5e4  (796 ) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02164) (UM: 0.00000) (S:  0.70239) (V:  -.----) 
info string c5f8  (707 ) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02209) (UM: 0.00000) (S:  0.70284) (V:  -.----) 
info string h4e4  (1129) N:       0 (+ 0) (P:  0.08%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02267) (UM: 0.00000) (S:  0.70342) (V:  -.----) 
info string d7d5  (293 ) N:       0 (+ 0) (P:  0.09%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02362) (UM: 0.00000) (S:  0.70437) (V:  -.----) 
info string c5b4  (726 ) N:       0 (+ 0) (P:  0.09%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02390) (UM: 0.00000) (S:  0.70465) (V:  -.----) 
info string c5a3  (730 ) N:       0 (+ 0) (P:  0.09%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02447) (UM: 0.00000) (S:  0.70521) (V:  -.----) 
info string h7h6  (400 ) N:       0 (+ 0) (P:  0.09%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02482) (UM: 0.00000) (S:  0.70557) (V:  -.----) 
info string c5d4  (728 ) N:       0 (+ 0) (P:  0.09%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02540) (UM: 0.00000) (S:  0.70615) (V:  -.----) 
info string h7h5  (403 ) N:       0 (+ 0) (P:  0.10%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02615) (UM: 0.00000) (S:  0.70689) (V:  -.----) 
info string c5e7  (712 ) N:       0 (+ 0) (P:  0.10%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.02622) (UM: 0.00000) (S:  0.70697) (V:  -.----) 
info string b7b6  (230 ) N:       0 (+ 0) (P:  0.11%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.03031) (UM: 0.00000) (S:  0.71106) (V:  -.----) 
info string b7a6  (229 ) N:       0 (+ 0) (P:  0.28%) (WL:  -.-----) (D: -.---) (M:  -.-) (Q:  0.68075) (U: 0.07504) (UM: 0.00000) (S:  0.75579) (V:  -.----) 
info string b8a6  (34  ) N:       0 (+ 1) (P:  3.20%) (WL:  0.00000) (D: 0.000) (M:  0.0) (Q:  0.00000) (U: 0.43076) (UM: 0.00000) (S:  1.11151) (V:  -.----) 
info string c5f2  (736 ) N:      85 (+ 0) (P: 34.36%) (WL:  1.00000) (D: 0.000) (M:  0.0) (Q:  1.00000) (U: 0.10753) (UM: 0.00272) (S:  1.11025) (V:  1.0000) (T) 
info string h4f2  (1135) N:     147 (+ 0) (P: 59.23%) (WL:  1.00000) (D: 0.000) (M:  0.0) (Q:  1.00000) (U: 0.10770) (UM: 0.00272) (S:  1.11042) (V:  1.0000) (T) 
info string node  (  47) N:     233 (+ 1) (P: 93.59%) (WL:  1.00000) (D: 0.000) (M:  1.0) (Q:  1.00000) (V:  0.9999) 
info string Best: h4f2
info string node  (   0) N:     147 (+ 0) (P:  0.00%) (WL: -1.00000) (D: 0.000) (M:  0.0) (Q: -1.00000) (V: -1.0000) (T)
bestmove h4f2""",
]


def send_command(command: str) -> None:
    """Send UCI commands to lichess-bot without output buffering."""
    print(command, flush=True)  # noqa: T201 (print() found)


send_command("id name UCI_Test_Bot")
send_command("id author lichess-bot-devs")
send_command("uciok")

board = chess.Board()
while True:
    command, *remaining = input().split()
    if command == "quit":
        break
    elif command == "isready":
        send_command("readyok")
    elif command == "position":
        spec_type, *remaining = remaining
        assert spec_type == "startpos"
        board = chess.Board()
        if remaining:
            moves_label, *move_list = remaining
            assert moves_label == "moves"
            for move in move_list:
                board.push_uci(move)
    elif command == "go":
        move_count = len(board.move_stack)
        move = verbose_stats[move_count]
        send_command(move)
