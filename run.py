from map_data import DataMapper
from get_images import save_images
#path='csv/corrupted_events_to_repair.csv'
#path='csv/69.csv'
path='csv/y_events.csv'
dm = DataMapper(path=path, hide_progress_bars=True, padding=20)

#for i in range(0,len(dm.gt_events)):
#    save_images(dm.gt_events[i].observations, index=i)

y_indices = [38,69,95,141,179,186,189,199,201,249,259,273,278,294,295,330,345,347,392,393,394,399,410,411,444,475,478,490,494,497,503,541,553,558,569,580,582,589,607,623,658,662,708,759,762,783,787,794,795,892,902,908,980,981,1001,1056,1059,1077,1078,1081,1101,1107,1108,1109,1110,1114,1120,1121,1131,1135,1144,1165,1318,1328,1369,1372,1383,1386,1391,1417,1441,1450,1469,1483,1485,1486,1487,1495,1496,1509,1523,1528,1535,1555,1585,1586,1597,1605,1614,1615,1626,1627,1636,1643,1653,1666,1674,1675,1682,1696,1709,1710,1712,1714,1735,1740,1753,1765,1770,1793,1813,1814,1815,1818,1819,1826,1833,1837,1839,1841,1860,1869,1873,1887,1890,1899,1903,1905,1913,1925,1931,1936,1945,1969,1993]
for i,j in enumerate(y_indices):
    save_images(dm.gt_events[i].observations, index=j)

# corrupt events
#indices = [315,  567, 838, 1166, 1311, 1664, 1666, 1668, 1928, 1937, 1938, 1952, 1983]
#for i,j in enumerate(indices):
#    save_images(dm.gt_events[i].observations, index=j)
