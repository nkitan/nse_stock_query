add_security = ("INSERT INTO Securities (symbol, cname, series, dateoflisting, paidupvalue, marketlot, isin, facevalue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
add_bhavcopy = ("INSERT INTO Bhavcopy (symbol, series, bopen, high, low, bclose, blast, prevclose, tottrdqty, tottrdval, btimestamp, totaltrades, isin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")