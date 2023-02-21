-- 식품분류별 가장 비싼 식품의 정보 조회하기
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY = '과자'
    OR CATEGORY = '국'
    OR CATEGORY = '김치'
    OR CATEGORY = '식용유')
    AND PRICE IN (
    SELECT MAX(PRICE)
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY)
GROUP BY 1
ORDER BY PRICE DESC;