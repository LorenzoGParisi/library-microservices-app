FROM maven:3-openjdk-17-slim as build
ADD ./src/ /usr/src/customer-spring/src
ADD ./pom.xml /usr/src/customer-spring
RUN mvn -f /usr/src/customer-spring/pom.xml clean package 

FROM openjdk:17
EXPOSE 8080
COPY --from=build /usr/src/customer-spring/target/customer-spring-0.0.1-SNAPSHOT.jar customer-spring.jar
ENTRYPOINT ["java", "-jar", "customer-spring.jar"]
