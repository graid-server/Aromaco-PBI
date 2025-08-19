# Aromaco Power BI – მონაცემთა მოდელი

## მთავარი ცხრილები
- **crm_deal** – გარიგებების ძირითადი ცხრილი (OPPORTUNITY, DATE_CREATE, ASSIGNED_BY_ID/NAME, CATEGORY_NAME, SOURCE_ID და სხვ.)
- **Calendar** – თარიღების ცხრილი (Year, Month, YearMonth)
- **crm_deal_uf** – ხელშეკრულებების დამატებითი ველები (მაგ: ხელშეკრულების დაწყების თარიღი)

## ძირითადი კავშირები
- crm_deal[DATE_CREATE] → Calendar[Date] (**Active relationship**)
- crm_deal_uf[ხელშეკრულების დაწყების თარიღი] → Calendar[Date] (**Inactive, საჭიროებისას USERELATIONSHIP**)
- სხვა თარიღები (BEGINDATE, CLOSEDATE, MODIFYDATE) → ინახება ლოკალურ Date ცხრილებთან

## Stage History
- Stage history დაკავშირებულია DEAL_ID–ზე
- გამოიყენება გარიგებების ეტაპების ხანგრძლივობისა და მოძრაობის ანალიზისთვის
