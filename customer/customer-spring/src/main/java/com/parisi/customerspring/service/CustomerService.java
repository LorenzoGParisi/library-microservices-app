package com.parisi.customerspring.service;

import java.util.List;

import com.parisi.customerspring.model.Customer;

public interface CustomerService {
	
	Customer createCustomer(Customer customer);
	List<Customer> getAllCustomer();
	Customer getCustomerById(long customerId);
	void deleteCustomer(long customerId);
}
