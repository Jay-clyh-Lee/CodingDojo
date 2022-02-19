<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<jsp:include page="includes/head.jsp"/>

<body>
    <main id="container" class="d-flex flex-column align-items-center justify-content-center">
        <div>
            <h1>All dojos</h1>
            <table class="table table-striped table-bordered text-center">
                <thead>
                    <tr>
                        <th>location</th>
          				<th>actions</th>
                    </tr>
                </thead>
                <tbody>
                	<c:forEach var="dojo" items="${dojos}">
                    	<tr>
                            <td><c:out value="${dojo.name}"/></td>
                    		<td>
	                            <a href="/dojo/view/${dojo.id}">view</a> |
	                            <a href="/dojo/delete/${dojo.id}">delete</a>
                        	</td>
                        </tr>
                    </c:forEach>
                </tbody>
            </table>
        </div>
        <div>
        	<a href="/dojo/add">Add a new dojo</a>
        	<a href="/ninja/add">Add a new ninja</a>
        </div>
    </main>
</body><td>
                    		
                        