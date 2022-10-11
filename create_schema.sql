CREATE DATABASE nse_stock_data;
USE nse_stock_data;

CREATE TABLE Securities (
    isin VARCHAR(12),
    symbol VARCHAR(256),
    cname VARCHAR(1024),
    series VARCHAR(20),
    dateoflisting DATE,
    paidupvalue MEDIUMINT,
    marketlot INT, 
    facevalue INT,
    PRIMARY KEY(isin)
);

CREATE TABLE Bhavcopy (
    isin VARCHAR(12),
    symbol VARCHAR(256),
    series VARCHAR(20),
    bopen INT,
    high INT,
    low INT,
    bclose INT,
    blast INT,
    prevclose INT,
    tottrdqty INT,
    tottrdval BIGINT,
    btimestamp DATE,
    totaltrades INT
);