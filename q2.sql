SELECT Name from Salesperson LEFT JOIN Orders on Salespersons.ID = Orders.salesperson_id
	where Orders.Amount >1300;