<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<jsp:include page="includes/head.jsp" />

<body>
	<main id="container" class="d-flex flex-column align-items-center justify-content-center">
		<div>
			<h1>New Dojo</h1>
			<form:form action="/dojo/create" method="post" modelAttribute="dojo">
			    <div class="form-group">
			        <form:label path="name">Name/Location:
			            <form:errors path="name"/>
			            <form:input type="text" path="name" class="form-control"/>
			        </form:label>
			    </div>
			    <input type="submit" value="Build" class="mt-3 btn-success"/>
			</form:form>
		</div>
		<div>
			<a href="/dojos">Go Back</a>
		</div>
	</main>
</body>
</html>