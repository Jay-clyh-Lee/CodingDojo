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
    <div class="d-flex justify-content-center">
		<div id="add_form" class="d-flex flex-column align-items-center mt-3">
			<h3>Add an Expense:</h2>
			<form:form action="/expenses" method="post" modelAttribute="expenses">
				<div class="form-group">
					<form:label path="name">Name:</form:label>
					<form:errors path="name" class="error"/>
					<form:input path="name" type="text" class="form-control"/>
				</div>
				<div class="form-group">
					<form:label path="vendor">Vendor:</form:label>
					<form:errors path="vendor" class="error"/>
					<form:input path="vendor" type="text" class="form-control"/>
				</div>
				<div class="form-group">
					<form:label path="amount">Cost:</form:label>
					<form:errors path="amount" class="error"/>
					<form:input path="amount" type="number" step="0.01" class="form-control"/>
				</div>
				<div class="form-group">
					<form:label path="description">Description:</form:label>
					<form:errors path="description" class="error"/>
					<form:input path="description" type="text" class="col-10 row-5 form-control"/>
				</div>
				<input type="submit" value="Add Expense" class="btn-primary"/>
			</form:form>
		</div>
	</div>
</body>
</html>

