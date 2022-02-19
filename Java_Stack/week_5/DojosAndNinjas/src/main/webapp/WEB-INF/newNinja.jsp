<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<jsp:include page="includes/head.jsp" />

<body>
	<main id="container" class="d-flex flex-column align-items-center justify-content-center">
	    <div>
		    <h1>New Ninja</h1>
		    <form:form action="/ninja/create" method="post" modelAttribute="ninja">
		        <div class="form-group">
		            <form:label path="dojo">Dojo:
		            	<form:select path="dojo">
		                    <c:forEach var="dojo" items="${dojos}">
		                        <option value="${dojo.id}">
		                            <c:out value="${dojo.name}" />
		                        </option>
		                    </c:forEach>
		                </form:select>
		            </form:label>
		        </div>
		        <div class="form-group">
		            <form:label path="firstName">First Name:
		                <form:errors path="firstName" />
		                <form:input type="text" path="firstName" class="form-control"/>
		            </form:label>
		        </div>
		        <div class="form-group">
		            <form:label path="lastName">Last Name:
		                <form:errors path="lastName" />
		                <form:input type="text" path="lastName" class="form-control"/>
		            </form:label>
		        </div>
		        <div class="form-group">
		            <form:label path="age">Age:
		                <form:errors path="age"/>
		                <form:input type="number" value="18" path="age" class="form-control"/>
		            </form:label>
		        </div>
		        <input type="submit" value="Submit" class="mt-3 btn-success"/>
		    </form:form>
	    </div>
	    <div>
			<a href="/dojos">Go Back</a>
		</div>
	</main>
</body>
</html>