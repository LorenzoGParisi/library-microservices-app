package com.parisi.customerspring.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.parisi.customerspring.exception.ResourceNotFoundException;
import com.parisi.customerspring.model.Customer;
import com.parisi.customerspring.repository.customerRepository;

@Service
@Transactional
public class CustomerServiceImpl implements CustomerService {
	
	@Autowired
	private customerRepository customerRepository;

	@Override
	public Customer createCustomer(Customer customer) {
		// TODO Auto-generated method stub
		return customerRepository.save(customer);
	}

	@Override
	public List<Customer> getAllCustomer() {
		// TODO Auto-generated method stub
		return this.customerRepository.findAll();
	}

	@Override
	public Customer getCustomerById(long customerId) {
		// TODO Auto-generated method stub
		Optional<Customer> customerDb = this.customerRepository.findById(customerId);
		if(customerDb.isPresent()) {
			return customerDb.get();
		} else {
			throw new ResourceNotFoundException("Record not found with id: " + customerId);
		}
	}

	@Override
	public void deleteCustomer(long customerId) {
		// TODO Auto-generated method stub
		Optional<Customer> customerDb = this.customerRepository.findById(customerId);
		if(customerDb.isPresent()) {
			this.customerRepository.delete(customerDb.get());
		} else {
			throw new ResourceNotFoundException("Record not found with id: " + customerId);
		}
	}
	
}
