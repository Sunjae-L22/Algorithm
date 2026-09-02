-- 프로그래머스 133024 — 인기있는 아이스크림
-- https://school.programmers.co.kr/learn/courses/30/lessons/133024

USE programmers;

DROP TABLE IF EXISTS FIRST_HALF;

CREATE TABLE FIRST_HALF (
    SHIPMENT_ID INT          NOT NULL PRIMARY KEY,
    FLAVOR      VARCHAR(255) NOT NULL,
    TOTAL_ORDER INT          NOT NULL
);

-- 문제 페이지 예제 데이터
INSERT INTO FIRST_HALF VALUES
(101, 'chocolate',       3200),
(102, 'vanilla',         2800),
(103, 'mint_chocolate',  1700),
(104, 'caramel',         2600),
(105, 'white_chocolate', 3100),
(106, 'peach',           2450),
(107, 'watermelon',      2150),
(108, 'mango',           2900),
(109, 'strawberry',      3100),
(110, 'melon',           3150),
(111, 'orange',          2900),
(112, 'pineapple',       2900);