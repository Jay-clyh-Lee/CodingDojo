<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<jsp:include page="includes/head.jsp" />

<body>
    <main id="container" class="d-flex flex-column align-items-center justify-content-center">
        <div id="form">
            <h1><c:out value="${dojo.name}"/> Coding Dojo</h1>
            <table class="table table-striped table-bordered">
                <thead>
                	<h3>Ninjas</h3>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Age</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <c:forEach var="ninja" items="${dojo.ninjas}">
                            <td><c:out value="${ninja.firstName}"/></td>
                            <td><c:out value="${ninja.lastName}"/></td>
                            <td><c:out value="${ninja.age}"/></td>
                        </c:forEach>
                    </tr>
                </tbody>
            </table>
        </div>
        <div>
			<a href="/dojos">Go Back</a>
		</div>
    </main>
</body>
</html>
</html>