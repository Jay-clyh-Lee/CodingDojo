# 1. What query would you run to get the total revenue for March of 2012?
SELECT SUM(amount) AS revenue, DATE_FORMAT(charged_datetime,'%M') AS month FROM billing 
WHERE DATE_FORMAT(charged_datetime,'%M %Y') LIKE "March 2012%";


# 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT client_id, SUM(amount) AS revenue FROM billing
WHERE client_id = 2;

# 3. What query would you run to get all the sites that client with an id of 10 owns?
SELECT domain_name AS websites, client_id FROM sites
WHERE client_id = 10;

# 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client with an id of 20?
SELECT client_id, COUNT(domain_name), DATE_FORMAT(created_datetime,'%M %Y') AS month FROM sites
WHERE client_id = 1
GROUP BY created_datetime;

# 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT domain_name AS websites, COUNT(*) FROM sites
WHERE created_datetime BETWEEN "2011-01-01" AND "2011-01-15"
GROUP BY domain_name;

SELECT domain_name AS websites, COUNT(*) FROM sites
WHERE created_datetime > "2011-01-01" AND created_datetime < "2011-01-15"
GROUP BY domain_name;

# 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS full_name, COUNT(clients.email) AS number_of_leads FROM clients
LEFT JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY full_name;

# 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT 
	CONCAT(clients.first_name, " ", clients.last_name) AS full_name, 
	COUNT(leads.registered_datetime) AS number_of_leads, DATE_FORMAT(registered_datetime, '%M') AS month_generated FROM clients
	LEFT JOIN sites ON sites.client_id = clients.client_id
	LEFT JOIN leads ON sites.site_id = leads.site_id
	WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-06-30"
    GROUP BY  leads.leads_id;  # group by leads_id because leads_id is unique. Groupy by name or month wouldn't work because they are not unique.

    
# 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

# 8.a
SELECT 
	clients.client_id,
	CONCAT(clients.first_name, " ", clients.last_name) AS client,
    domain_name AS website,
	COUNT(leads.registered_datetime) AS number_of_leads, DATE_FORMAT(registered_datetime, '%M') AS month_generated FROM clients
	LEFT JOIN sites ON sites.client_id = clients.client_id
	LEFT JOIN leads ON sites.site_id = leads.site_id
	WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
    GROUP BY website
    ORDER BY clients.client_id, website;
    
# 8.b
SELECT 
	clients.client_id,
	CONCAT(clients.first_name, " ", clients.last_name) AS client,
    domain_name AS website,
	COUNT(leads.registered_datetime) AS number_of_leads, DATE_FORMAT(registered_datetime, '%M') AS month_generated FROM clients
	LEFT JOIN sites ON sites.client_id = clients.client_id
	LEFT JOIN leads ON sites.site_id = leads.site_id
    GROUP BY website
    ORDER BY clients.client_id, website;


# 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.  First try this with integer month, second with month name.  A SELECT subquery will be needed for the second challenge.  Look at this for a hint.

# 9.a
SELECT 
	clients.client_id,
	CONCAT(clients.first_name, " ", clients.last_name) AS client,
    SUM(amount) AS total,
    DATE_FORMAT(charged_datetime, '%m') AS month,
    DATE_FORMAT(charged_datetime, '%Y') AS year
    FROM billing
	LEFT JOIN clients ON clients.client_id = billing.client_id
	GROUP BY year, month
	ORDER BY clients.client_id;
    
#9.b
SELECT 
	clients.client_id,
	CONCAT(clients.first_name, " ", clients.last_name) AS client,
    SUM(amount) AS total,
    DATE_FORMAT(charged_datetime, '%M') AS month,
    DATE_FORMAT(charged_datetime, '%Y') AS year
    FROM billing
	LEFT JOIN clients ON clients.client_id = billing.client_id
	GROUP BY year, month
	ORDER BY clients.client_id;


# 10. Write a single query that retrieves all the sites that each client owns. Group the results so that all of the sites for each client are displayed in a single field. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT 
	CONCAT(clients.first_name, " ", clients.last_name) AS client, 
    GROUP_CONCAT(domain_name SEPARATOR ' / ') AS sites FROM clients
	LEFT JOIN sites ON sites.client_id = clients.client_id
    GROUP BY client
    ORDER BY clients.client_id;
