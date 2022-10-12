CREATE DATABASE nse_stock_data;
USE nse_stock_data;

CREATE TABLE Securities (
    isin VARCHAR(12),
    symbol VARCHAR(256),
    cname VARCHAR(1024),
    series VARCHAR(20),
    dateoflisting DATE,
    paidupvalue MEDIUMINT,
    marketlot FLOAT, 
    facevalue FLOAT,
    PRIMARY KEY(isin)
);

CREATE TABLE Bhavcopy (
    isin VARCHAR(12),
    symbol VARCHAR(256),
    series VARCHAR(20),
    bopen FLOAT,
    high FLOAT,
    low FLOAT,
    bclose FLOAT,
    blast FLOAT,
    prevclose FLOAT,
    tottrdqty FLOAT,
    tottrdval BIGINT,
    btimestamp DATE,
    totaltrades INT
);