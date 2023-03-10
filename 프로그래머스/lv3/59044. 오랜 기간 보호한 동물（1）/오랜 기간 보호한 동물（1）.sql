-- 오랜 기간 보호한 동물(1)
SELECT T1.NAME, T1.DATETIME
FROM ANIMAL_INS AS T1
LEFT JOIN ANIMAL_OUTS AS T2
    ON T1.ANIMAL_ID = T2.ANIMAL_ID
WHERE T2.DATETIME IS NULL
    AND T1.NAME IN (
        SELECT T1.NAME
        FROM (
            SELECT T1.NAME
            FROM ANIMAL_INS AS T1
            INNER JOIN ANIMAL_OUTS AS T2
                ON T1.ANIMAL_ID = T2.ANIMAL_ID
            ORDER BY DATEDIFF(T2.DATETIME, T1.DATETIME)
            LIMIT 3) TEMP
)
ORDER BY T1.DATETIME
LIMIT 3;