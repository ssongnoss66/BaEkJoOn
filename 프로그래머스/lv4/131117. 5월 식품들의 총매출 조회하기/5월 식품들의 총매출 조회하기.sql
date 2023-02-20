-- 5월 식품들의 총매출 조회하기
SELECT FOOD_PRODUCT.PRODUCT_ID, PRODUCT_NAME, SUM(PRICE * AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT
INNER JOIN FOOD_ORDER
    ON FOOD_PRODUCT.PRODUCT_ID = FOOD_ORDER.PRODUCT_ID
WHERE DATE_FORMAT(PRODUCE_DATE,'%Y-%m')='2022-05'
GROUP BY FOOD_ORDER.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID;