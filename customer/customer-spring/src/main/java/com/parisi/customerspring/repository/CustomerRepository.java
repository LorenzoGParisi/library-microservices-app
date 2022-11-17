package com.parisi.customerspring.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.parisi.customerspring.model.Customer;

public interface CustomerRepository extends MongoRepository<Customer , Long>{

}
