<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
	<link rel="stylesheet" href="/css/style.css">
	<title>Save Travel</title>
    <style>
        p {
            font-weight: bold;
        }
        a {
            text-decoration: none;
            margin: 1em;
            font-weight: 500;
        }
    </style>
</head>
<body class="mx-auto">
    <main class="d-flex justify-content-center mt-3">
        <div id="table">
            <h1 style="color:skyblue">Save Travel</h1>
            <table class="table">
                <thead>
                    <th>Expense</th>
                    <th>Vendor</th>
                    <th>Amount</th>
                    <th>Actions</th>
                </thead>
                <c:forEach var="expense" items="${expenses}">
                    <tr>
                    	<td>
                    		<a href="/expense/view/<c:out value='${expense.id}'/>">
                    			<c:out value="${expense.name}"/>
                    		</a>
                    	</td>
                        <td>
                            <c:out value="${expense.vendor}"/>
                        </td>
                        <td>
                            <c:out value="${expense.amount}"/>
                        </td>
                        <td>
                            <a href="/expense/edit/${expense.id}">edit</a> |
                            <a href="/expense/delete/${expense.id}">delete</a>
                        </td>
                    </tr>
                </c:forEach>
            </table>
        </div>
    </main>

    <div class="d-flex justify-content-center">
		<div id="add_form" class="d-flex flex-column align-items-center mt-3">
			<h2>Add an Expense:</h2>
			<form:form action="/expense/create" method="post" modelAttribute="expense">
				<div class="form-group">
					<form:label path="name">Name:
						<form:errors path="name" class="error"/>
						<form:input type="text" path="name" class="form-control"/>
					</form:label>
				</div>
				<div class="form-group">
					<form:label path="vendor">Vendor:
						<form:errors path="vendor" class="error"/>
						<form:input type="text" path="vendor" class="form-control"/>
					</form:label>
				</div>
				<div class="form-group">
					<form:label path="amount">Cost:
						<form:errors path="amount" class="error"/>
						<form:input type="number" step="0.01" path="amount" class="form-control"/>
					</form:label>
				</div>
				<div class="form-group">
					<form:label path="description">Description:
						<form:errors path="description" class="error"/>
						<form:input type="text" path="description" class="col-10 row-5 form-control"/>
					</form:label>
				</div>
				<input type="submit" value="Add Expense" class="btn-warning mt-3"/>
			</form:form>
		</div>
	</div>
</body>
</html>

