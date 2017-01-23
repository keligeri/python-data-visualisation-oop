CREATE OR REPLACE VIEW from_gbp AS SELECT name, ((budget_value::float) * 1.15212953) as budget, main_color, id
FROM project
WHERE budget_currency LIKE 'GBP' 
AND name || main_color is NOT NULL
ORDER BY budget DESC;

CREATE OR REPLACE VIEW from_usd AS SELECT name, ((budget_value::float) * 0.947404821) as budget, main_color, id
FROM project
WHERE budget_currency LIKE 'USD' 
AND name || main_color is NOT NULL
ORDER BY budget DESC;

CREATE OR REPLACE VIEW from_eur AS SELECT name, budget_value::float as budget, main_color, id
FROM project
WHERE budget_currency LIKE 'EUR' 
AND name || main_color is NOT NULL
ORDER BY budget DESC;

CREATE OR REPLACE VIEW budget_in_eur AS
SELECT * FROM from_eur
UNION
SELECT * FROM from_usd
UNION
SELECT * from from_gbp;

SELECT name, budget, main_color FROM budget_in_eur
ORDER BY budget DESC;