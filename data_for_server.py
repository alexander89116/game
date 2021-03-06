GAME_SPEED = 40

PRICE_NEW_CITY = 100

POPULATION_NEW_CITY = 13

RESOURCE_NAME = ['wood', 'stone', 'silver', 'pop']

FARM_LVL = [{"wood": 0, "stone": 0, "silver": 0, "max_population": 114, "delta": 7, "pop": 0},
            {"wood": 5, "stone": 4, "silver": 1, "max_population": 121, "delta": 7, "pop": 0},
            {"wood": 24, "stone": 18, "silver": 5, "max_population": 134, "delta": 13, "pop": 0},
            {"wood": 64, "stone": 49, "silver": 16, "max_population": 152, "delta": 18, "pop": 0},
            {"wood": 129, "stone": 104, "silver": 38, "max_population": 175, "delta": 23, "pop": 0},
            {"wood": 228, "stone": 190, "silver": 74, "max_population": 206, "delta": 31, "pop": 0},
            {"wood": 304, "stone": 260, "silver": 107, "max_population": 245, "delta": 39, "pop": 0},
            {"wood": 391, "stone": 341, "silver": 147, "max_population": 291, "delta": 46, "pop": 0},
            {"wood": 487, "stone": 433, "silver": 195, "max_population": 341, "delta": 50, "pop": 0},
            {"wood": 593, "stone": 536, "silver": 251, "max_population": 399, "delta": 58, "pop": 0},
            {"wood": 709, "stone": 650, "silver": 316, "max_population": 458, "delta": 59, "pop": 0},
            {"wood": 834, "stone": 776, "silver": 389, "max_population": 520, "delta": 62, "pop": 0},
            {"wood": 969, "stone": 913, "silver": 471, "max_population": 584, "delta": 64, "pop": 0},
            {"wood": 1113, "stone": 1061, "silver": 563, "max_population": 651, "delta": 67, "pop": 0},
            {"wood": 1266, "stone": 1220, "silver": 665, "max_population": 720, "delta": 69, "pop": 0},
            {"wood": 1428, "stone": 1391, "silver": 776, "max_population": 790, "delta": 70, "pop": 0},
            {"wood": 1600, "stone": 1573, "silver": 898, "max_population": 863, "delta": 73, "pop": 0},
            {"wood": 1780, "stone": 1767, "silver": 1030, "max_population": 938, "delta": 75, "pop": 0},
            {"wood": 1970, "stone": 1972, "silver": 1172, "max_population": 1015, "delta": 77, "pop": 0},
            {"wood": 2168, "stone": 2188, "silver": 1326, "max_population": 1094, "delta": 79, "pop": 0},
            {"wood": 2375, "stone": 2416, "silver": 1490, "max_population": 1174, "delta": 80, "pop": 0},
            {"wood": 2591, "stone": 2655, "silver": 1667, "max_population": 1257, "delta": 83, "pop": 0},
            {"wood": 2815, "stone": 2906, "silver": 1854, "max_population": 1341, "delta": 84, "pop": 0},
            {"wood": 3048, "stone": 3168, "silver": 2054, "max_population": 1426, "delta": 85, "pop": 0},
            {"wood": 3290, "stone": 3442, "silver": 2265, "max_population": 1514, "delta": 88, "pop": 0},
            {"wood": 3541, "stone": 3727, "silver": 2488, "max_population": 1602, "delta": 88, "pop": 0},
            {"wood": 3800, "stone": 4024, "silver": 2724, "max_population": 1693, "delta": 91, "pop": 0},
            {"wood": 4067, "stone": 4332, "silver": 2973, "max_population": 1785, "delta": 92, "pop": 0},
            {"wood": 4343, "stone": 4652, "silver": 3234, "max_population": 1878, "delta": 93, "pop": 0},
            {"wood": 4627, "stone": 4983, "silver": 3508, "max_population": 1973, "delta": 95, "pop": 0},
            {"wood": 4920, "stone": 5326, "silver": 3795, "max_population": 2070, "delta": 97, "pop": 0},
            {"wood": 5221, "stone": 5681, "silver": 4096, "max_population": 2168, "delta": 98, "pop": 0},
            {"wood": 5530, "stone": 6047, "silver": 4410, "max_population": 2267, "delta": 99, "pop": 0},
            {"wood": 5847, "stone": 6425, "silver": 4738, "max_population": 2368, "delta": 101, "pop": 0},
            {"wood": 6173, "stone": 6814, "silver": 5079, "max_population": 2470, "delta": 102, "pop": 0},
            {"wood": 6507, "stone": 7215, "silver": 5434, "max_population": 2573, "delta": 103, "pop": 0},
            {"wood": 6849, "stone": 7628, "silver": 5803, "max_population": 2678, "delta": 105, "pop": 0},
            {"wood": 7199, "stone": 8052, "silver": 6187, "max_population": 2784, "delta": 106, "pop": 0},
            {"wood": 7558, "stone": 8489, "silver": 6585, "max_population": 2891, "delta": 107, "pop": 0},
            {"wood": 7924, "stone": 8936, "silver": 6998, "max_population": 3000, "delta": 109, "pop": 0},
            {"wood": 8298, "stone": 9396, "silver": 7425, "max_population": 3109, "delta": 109, "pop": 0},
            {"wood": 8681, "stone": 9867, "silver": 7867, "max_population": 3220, "delta": 111, "pop": 0},
            {"wood": 9071, "stone": 10349, "silver": 8324, "max_population": 3332, "delta": 112, "pop": 0},
            {"wood": 9470, "stone": 10844, "silver": 8796, "max_population": 3446, "delta": 114, "pop": 0},
            {"wood": 9876, "stone": 11350, "silver": 9283, "max_population": 3561, "delta": 115, "pop": 0}]

SAWMILL_LVL = [{"wood": 3, "stone": 2, "silver": 1, "pop": 1, "output": 8},
               {"wood": 10, "stone": 9, "silver": 6, "pop": 2, "output": 12},
               {"wood": 21, "stone": 20, "silver": 15, "pop": 2, "output": 18},
               {"wood": 36, "stone": 37, "silver": 27, "pop": 2, "output": 24},
               {"wood": 55, "stone": 59, "silver": 44, "pop": 2, "output": 30},
               {"wood": 78, "stone": 86, "silver": 64, "pop": 2, "output": 37},
               {"wood": 105, "stone": 119, "silver": 89, "pop": 2, "output": 43},
               {"wood": 135, "stone": 158, "silver": 117, "pop": 3, "output": 51},
               {"wood": 169, "stone": 202, "silver": 150, "pop": 3, "output": 58},
               {"wood": 207, "stone": 252, "silver": 188, "pop": 3, "output": 66},
               {"wood": 248, "stone": 308, "silver": 229, "pop": 3, "output": 73},
               {"wood": 292, "stone": 369, "silver": 275, "pop": 3, "output": 81},
               {"wood": 340, "stone": 437, "silver": 325, "pop": 3, "output": 89},
               {"wood": 391, "stone": 510, "silver": 380, "pop": 3, "output": 98},
               {"wood": 446, "stone": 590, "silver": 440, "pop": 3, "output": 106},
               {"wood": 504, "stone": 676, "silver": 503, "pop": 3, "output": 114},
               {"wood": 566, "stone": 767, "silver": 572, "pop": 3, "output": 123},
               {"wood": 631, "stone": 865, "silver": 645, "pop": 3, "output": 132},
               {"wood": 699, "stone": 969, "silver": 722, "pop": 3, "output": 141},
               {"wood": 771, "stone": 1079, "silver": 804, "pop": 3, "output": 150},
               {"wood": 846, "stone": 1196, "silver": 891, "pop": 3, "output": 159},
               {"wood": 924, "stone": 1319, "silver": 982, "pop": 3, "output": 168},
               {"wood": 1005, "stone": 1448, "silver": 1078, "pop": 3, "output": 178},
               {"wood": 1090, "stone": 1583, "silver": 1179, "pop": 3, "output": 187},
               {"wood": 1178, "stone": 1725, "silver": 1285, "pop": 3, "output": 197},
               {"wood": 1269, "stone": 1873, "silver": 1395, "pop": 3, "output": 206},
               {"wood": 1363, "stone": 2027, "silver": 1510, "pop": 3, "output": 216},
               {"wood": 1461, "stone": 2188, "silver": 1630, "pop": 3, "output": 226},
               {"wood": 1561, "stone": 2355, "silver": 1755, "pop": 3, "output": 236},
               {"wood": 1665, "stone": 2529, "silver": 1884, "pop": 3, "output": 246},
               {"wood": 1772, "stone": 2710, "silver": 2019, "pop": 3, "output": 256},
               {"wood": 1883, "stone": 2896, "silver": 2158, "pop": 3, "output": 266},
               {"wood": 1996, "stone": 3090, "silver": 2302, "pop": 3, "output": 276},
               {"wood": 2112, "stone": 3290, "silver": 2451, "pop": 4, "output": 286},
               {"wood": 2232, "stone": 3496, "silver": 2605, "pop": 4, "output": 297},
               {"wood": 2355, "stone": 3709, "silver": 2763, "pop": 4, "output": 307},
               {"wood": 2481, "stone": 3929, "silver": 2927, "pop": 4, "output": 318},
               {"wood": 2610, "stone": 4155, "silver": 3096, "pop": 4, "output": 328},
               {"wood": 2742, "stone": 4388, "silver": 3269, "pop": 4, "output": 339},
               {"wood": 2877, "stone": 4628, "silver": 3448, "pop": 4, "output": 350}]

QUARRY_LVL = [{"wood": 1, "stone": 3, "silver": 2, "pop": 1, "output": 8},
              {"wood": 6, "stone": 10, "silver": 10, "pop": 2, "output": 12},
              {"wood": 13, "stone": 21, "silver": 24, "pop": 2, "output": 18},
              {"wood": 24, "stone": 36, "silver": 44, "pop": 2, "output": 24},
              {"wood": 38, "stone": 55, "silver": 70, "pop": 2, "output": 30},
              {"wood": 56, "stone": 78, "silver": 103, "pop": 2, "output": 37},
              {"wood": 77, "stone": 105, "silver": 143, "pop": 2, "output": 43},
              {"wood": 102, "stone": 135, "silver": 189, "pop": 3, "output": 51},
              {"wood": 131, "stone": 169, "silver": 242, "pop": 3, "output": 58},
              {"wood": 164, "stone": 207, "silver": 302, "pop": 3, "output": 66},
              {"wood": 200, "stone": 248, "silver": 369, "pop": 3, "output": 73},
              {"wood": 240, "stone": 292, "silver": 443, "pop": 3, "output": 81},
              {"wood": 284, "stone": 340, "silver": 524, "pop": 3, "output": 89},
              {"wood": 332, "stone": 391, "silver": 612, "pop": 3, "output": 98},
              {"wood": 383, "stone": 446, "silver": 708, "pop": 3, "output": 106},
              {"wood": 439, "stone": 504, "silver": 811, "pop": 3, "output": 115},
              {"wood": 499, "stone": 566, "silver": 921, "pop": 3, "output": 123},
              {"wood": 562, "stone": 631, "silver": 1038, "pop": 3, "output": 132},
              {"wood": 630, "stone": 699, "silver": 1163, "pop": 3, "output": 141},
              {"wood": 702, "stone": 771, "silver": 1295, "pop": 3, "output": 150},
              {"wood": 777, "stone": 846, "silver": 1435, "pop": 3, "output": 159},
              {"wood": 857, "stone": 924, "silver": 1582, "pop": 3, "output": 168},
              {"wood": 941, "stone": 1005, "silver": 1737, "pop": 3, "output": 178},
              {"wood": 1029, "stone": 1090, "silver": 1900, "pop": 3, "output": 187},
              {"wood": 1121, "stone": 1178, "silver": 2070, "pop": 3, "output": 197},
              {"wood": 1217, "stone": 1269, "silver": 2247, "pop": 3, "output": 206},
              {"wood": 1318, "stone": 1363, "silver": 2433, "pop": 3, "output": 216},
              {"wood": 1422, "stone": 1461, "silver": 2626, "pop": 3, "output": 226},
              {"wood": 1531, "stone": 1561, "silver": 2826, "pop": 3, "output": 236},
              {"wood": 1644, "stone": 1665, "silver": 3035, "pop": 3, "output": 246},
              {"wood": 1761, "stone": 1772, "silver": 3251, "pop": 3, "output": 256},
              {"wood": 1883, "stone": 1883, "silver": 3476, "pop": 3, "output": 266},
              {"wood": 2008, "stone": 1996, "silver": 3708, "pop": 3, "output": 276},
              {"wood": 2138, "stone": 2112, "silver": 3947, "pop": 4, "output": 286},
              {"wood": 2272, "stone": 2232, "silver": 4195, "pop": 4, "output": 297},
              {"wood": 2411, "stone": 2355, "silver": 4451, "pop": 4, "output": 307},
              {"wood": 2556, "stone": 2482, "silver": 4714, "pop": 4, "output": 318},
              {"wood": 2701, "stone": 2610, "silver": 4986, "pop": 4, "output": 328},
              {"wood": 2852, "stone": 2742, "silver": 5266, "pop": 4, "output": 339},
              {"wood": 3008, "stone": 2877, "silver": 5553, "pop": 4, "output": 350}]

MINE_LVL = [{"wood": 5, "stone": 2, "silver": 4, "pop": 1, "output": 8},
            {"wood": 19, "stone": 8, "silver": 14, "pop": 2, "output": 12},
            {"wood": 40, "stone": 18, "silver": 29, "pop": 2, "output": 18},
            {"wood": 70, "stone": 32, "silver": 49, "pop": 2, "output": 24},
            {"wood": 106, "stone": 50, "silver": 72, "pop": 2, "output": 30},
            {"wood": 150, "stone": 72, "silver": 101, "pop": 2, "output": 37},
            {"wood": 202, "stone": 98, "silver": 133, "pop": 2, "output": 43},
            {"wood": 260, "stone": 128, "silver": 169, "pop": 3, "output": 51},
            {"wood": 325, "stone": 162, "silver": 209, "pop": 3, "output": 58},
            {"wood": 397, "stone": 200, "silver": 252, "pop": 3, "output": 66},
            {"wood": 476, "stone": 242, "silver": 300, "pop": 3, "output": 73},
            {"wood": 562, "stone": 288, "silver": 350, "pop": 3, "output": 81},
            {"wood": 654, "stone": 338, "silver": 405, "pop": 3, "output": 89},
            {"wood": 753, "stone": 392, "silver": 462, "pop": 3, "output": 98},
            {"wood": 858, "stone": 450, "silver": 524, "pop": 3, "output": 106},
            {"wood": 970, "stone": 512, "silver": 588, "pop": 3, "output": 115},
            {"wood": 1088, "stone": 578, "silver": 656, "pop": 3, "output": 123},
            {"wood": 1213, "stone": 648, "silver": 727, "pop": 3, "output": 132},
            {"wood": 1345, "stone": 722, "silver": 801, "pop": 3, "output": 141},
            {"wood": 1482, "stone": 800, "silver": 879, "pop": 3, "output": 150},
            {"wood": 1626, "stone": 882, "silver": 960, "pop": 3, "output": 159},
            {"wood": 1777, "stone": 968, "silver": 1043, "pop": 3, "output": 168},
            {"wood": 1933, "stone": 1058, "silver": 1130, "pop": 3, "output": 178},
            {"wood": 2096, "stone": 1152, "silver": 1220, "pop": 3, "output": 187},
            {"wood": 2265, "stone": 1250, "silver": 1313, "pop": 3, "output": 197},
            {"wood": 2440, "stone": 1352, "silver": 1409, "pop": 3, "output": 206},
            {"wood": 2622, "stone": 1458, "silver": 1508, "pop": 3, "output": 216},
            {"wood": 2809, "stone": 1568, "silver": 1610, "pop": 3, "output": 226},
            {"wood": 3003, "stone": 1682, "silver": 1715, "pop": 3, "output": 236},
            {"wood": 3203, "stone": 1800, "silver": 1823, "pop": 3, "output": 246},
            {"wood": 3408, "stone": 1922, "silver": 1934, "pop": 3, "output": 256},
            {"wood": 3620, "stone": 2048, "silver": 2028, "pop": 3, "output": 266},
            {"wood": 3838, "stone": 2178, "silver": 2165, "pop": 3, "output": 276},
            {"wood": 4062, "stone": 2312, "silver": 2284, "pop": 4, "output": 286},
            {"wood": 4292, "stone": 2450, "silver": 2406, "pop": 4, "output": 297},
            {"wood": 4528, "stone": 2592, "silver": 2532, "pop": 4, "output": 307},
            {"wood": 4770, "stone": 2738, "silver": 2660, "pop": 4, "output": 318},
            {"wood": 5018, "stone": 2888, "silver": 2790, "pop": 4, "output": 328},
            {"wood": 5272, "stone": 3042, "silver": 2924, "pop": 4, "output": 339},
            {"wood": 5532, "stone": 3200, "silver": 3060, "pop": 4, "output": 350}]

WAREHOUSE_LVL = [{"wood": 0, "stone": 0, "silver": 0, "pop": 0, "storage": 3100, "stash": 100},
                 {"wood": 10, "stone": 15, "silver": 4, "pop": 0, "storage": 3922, "stash": 200},
                 {"wood": 37, "stone": 58, "silver": 18, "pop": 0, "storage": 4870, "stash": 300},
                 {"wood": 115, "stone": 180, "silver": 60, "pop": 0, "storage": 5912, "stash": 400},
                 {"wood": 242, "stone": 381, "silver": 130, "pop": 0, "storage": 7034, "stash": 500},
                 {"wood": 426, "stone": 670, "silver": 235, "pop": 0, "storage": 8224, "stash": 600},
                 {"wood": 674, "stone": 1059, "silver": 379, "pop": 0, "storage": 9474, "stash": 700},
                 {"wood": 826, "stone": 1297, "silver": 473, "pop": 0, "storage": 10780, "stash": 800},
                 {"wood": 987, "stone": 1552, "silver": 576, "pop": 0, "storage": 12136, "stash": 900},
                 {"wood": 1159, "stone": 1821, "silver": 686, "pop": 0, "storage": 13536, "stash": 1000},
                 {"wood": 1340, "stone": 2105, "silver": 803, "pop": 0, "storage": 14982, "stash": 1100},
                 {"wood": 1529, "stone": 2403, "silver": 928, "pop": 0, "storage": 16468, "stash": 1200},
                 {"wood": 1727, "stone": 2714, "silver": 1060, "pop": 0, "storage": 17992, "stash": 1300},
                 {"wood": 1933, "stone": 3037, "silver": 1199, "pop": 0, "storage": 19552, "stash": 1400},
                 {"wood": 2146, "stone": 3373, "silver": 1344, "pop": 0, "storage": 21148, "stash": 1500},
                 {"wood": 2368, "stone": 3721, "silver": 1496, "pop": 0, "storage": 22776, "stash": 1600},
                 {"wood": 2596, "stone": 4080, "silver": 1654, "pop": 0, "storage": 24438, "stash": 1700},
                 {"wood": 2832, "stone": 4450, "silver": 1819, "pop": 0, "storage": 26130, "stash": 1800},
                 {"wood": 3074, "stone": 4831, "silver": 1990, "pop": 0, "storage": 27850, "stash": 1900},
                 {"wood": 3324, "stone": 5223, "silver": 2167, "pop": 0, "storage": 29600, "stash": 2000},
                 {"wood": 3580, "stone": 5625, "silver": 2349, "pop": 0, "storage": 31378, "stash": 2100},
                 {"wood": 3842, "stone": 6037, "silver": 2538, "pop": 0, "storage": 33182, "stash": 2200},
                 {"wood": 4110, "stone": 6459, "silver": 2732, "pop": 0, "storage": 35014, "stash": 2300},
                 {"wood": 4385, "stone": 6891, "silver": 2933, "pop": 0, "storage": 36870, "stash": 2400},
                 {"wood": 4666, "stone": 7332, "silver": 3138, "pop": 0, "storage": 38750, "stash": 2500},
                 {"wood": 4953, "stone": 7783, "silver": 3349, "pop": 0, "storage": 40654, "stash": 2600},
                 {"wood": 5245, "stone": 8242, "silver": 3566, "pop": 0, "storage": 42582, "stash": 2700},
                 {"wood": 5543, "stone": 8710, "silver": 3788, "pop": 0, "storage": 44532, "stash": 2800},
                 {"wood": 5847, "stone": 9188, "silver": 4015, "pop": 0, "storage": 46506, "stash": 2900},
                 {"wood": 6156, "stone": 9674, "silver": 4247, "pop": 0, "storage": 45500, "stash": 3000},
                 {"wood": 6470, "stone": 10168, "silver": 4485, "pop": 0, "storage": 50516, "stash": 3100},
                 {"wood": 6790, "stone": 10671, "silver": 4728, "pop": 0, "storage": 52552, "stash": 3200},
                 {"wood": 7116, "stone": 11182, "silver": 4975, "pop": 0, "storage": 54610, "stash": 3300},
                 {"wood": 7446, "stone": 11701, "silver": 5228, "pop": 0, "storage": 56686, "stash": 3400},
                 {"wood": 7781, "stone": 12228, "silver": 5486, "pop": 0, "storage": 58784, "stash": 3500}]

WALL_LVL = [{"wood": 0, "stone": 0, "silver": 0, "pop": 0, "bonus": 0},
            {"wood": 400, "stone": 350, "silver": 200, "pop": 2.0, "bonus": 3.7},
            {"wood": 400, "stone": 700, "silver": 429, "pop": 4.5, "bonus": 7.5},
            {"wood": 400, "stone": 1050, "silver": 670, "pop": 7.2, "bonus": 11.4},
            {"wood": 400, "stone": 1400, "silver": 919, "pop": 10.0, "bonus": 15.5},
            {"wood": 400, "stone": 1750, "silver": 1175, "pop": 12.9, "bonus": 19.7},
            {"wood": 400, "stone": 2100, "silver": 1435, "pop": 16.0, "bonus": 24.1},
            {"wood": 400, "stone": 2450, "silver": 1701, "pop": 19.1, "bonus": 28.5},
            {"wood": 400, "stone": 2800, "silver": 1970, "pop": 22.3, "bonus": 33.3},
            {"wood": 400, "stone": 3150, "silver": 2242, "pop": 25.6, "bonus": 38.0},
            {"wood": 400, "stone": 3500, "silver": 2518, "pop": 28.9, "bonus": 43.0},
            {"wood": 400, "stone": 3850, "silver": 2796, "pop": 32.3, "bonus": 48.1},
            {"wood": 400, "stone": 4200, "silver": 3077, "pop": 35.7, "bonus": 53.5},
            {"wood": 400, "stone": 4550, "silver": 3360, "pop": 39.2, "bonus": 59.0},
            {"wood": 400, "stone": 4900, "silver": 3646, "pop": 42.7, "bonus": 64.7},
            {"wood": 400, "stone": 5250, "silver": 3933, "pop": 46.3, "bonus": 70.5},
            {"wood": 400, "stone": 5600, "silver": 4222, "pop": 49.9, "bonus": 76.7},
            {"wood": 400, "stone": 5950, "silver": 4514, "pop": 53.5, "bonus": 82.9},
            {"wood": 400, "stone": 6300, "silver": 4807, "pop": 57.2, "bonus": 89.5},
            {"wood": 400, "stone": 6650, "silver": 5101, "pop": 60.9, "bonus": 96.2},
            {"wood": 400, "stone": 7000, "silver": 5397, "pop": 64.6, "bonus": 103.3},
            {"wood": 400, "stone": 7350, "silver": 5695, "pop": 68.4, "bonus": 110.4},
            {"wood": 400, "stone": 7700, "silver": 5994, "pop": 72.2, "bonus": 117.9},
            {"wood": 400, "stone": 8050, "silver": 6294, "pop": 76.0, "bonus": 125.6},
            {"wood": 400, "stone": 8400, "silver": 6596, "pop": 79.8, "bonus": 133.6},
            {"wood": 400, "stone": 8750, "silver": 6899, "pop": 83.7, "bonus": 141.9}]
