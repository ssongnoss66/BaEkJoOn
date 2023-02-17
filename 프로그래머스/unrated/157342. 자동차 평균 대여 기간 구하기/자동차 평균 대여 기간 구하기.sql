-- 자동차 평균 대여 기간 구하기

SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7.00
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;