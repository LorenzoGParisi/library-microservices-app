package com.parisi.customerspring.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.parisi.customerspring.model.Customer;

public interface customerRepository extends MongoRepository<Customer , Long>{

}
