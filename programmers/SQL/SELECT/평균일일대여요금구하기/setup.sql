-- 프로그래머스 151136 — 평균 일일 대여 요금 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/151136

CREATE DATABASE IF NOT EXISTS programmers;
USE programmers;
DROP TABLE IF EXISTS CAR_RENTAL_COMPANY_CAR;

CREATE TABLE CAR_RENTAL_COMPANY_CAR (
    CAR_ID    INTEGER      NOT NULL PRIMARY KEY,
    CAR_TYPE  VARCHAR(255) NOT NULL,
    DAILY_FEE INTEGER      NOT NULL,
    OPTIONS   VARCHAR(255) NOT NULL
);

-- 문제 페이지 예제 데이터
INSERT INTO CAR_RENTAL_COMPANY_CAR VALUES
(1, '세단', 16000, '가죽시트,열선시트,후방카메라'),
(2, 'SUV', 14000, '스마트키,네비게이션,열선시트'),
(3, 'SUV', 22000, '주차감지센서,네비게이션,스마트키,후방카메라');