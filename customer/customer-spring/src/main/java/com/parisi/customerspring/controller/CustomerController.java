package com.parisi.customerspring.controller;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.parisi.customerspring.model.Customer;
import com.parisi.customerspring.service.CustomerService;
import com.parisi.customerspring.service.SequenceGeneratorService;

@RestController 
public class CustomerController {
	
	@Autowired
	private CustomerService customerService;
	
	@Autowired
	private SequenceGeneratorService sequenceGeneratorService;
	
	@GetMapping("/customers")
	public ResponseEntity<List<Customer>> getAllCustomer(){
		return ResponseEntity.ok().body(customerService.getAllCustomer());
	}
	
	@GetMapping("/customers/{id}")
	public ResponseEntity<Customer> getCustomerById(@PathVariable long id){
		return ResponseEntity.ok().body(customerService.getCustomerById(id));
	}
	
	@PostMapping("/customers")
	public ResponseEntity<Customer> createCustomer(@Valid @RequestBody Customer customer){
		customer.setCustomerId(sequenceGeneratorService.generateSequence(Customer.SEQUENCE_NAME));
		return ResponseEntity.ok().body(this.customerService.createCustomer(customer));
	}
	
	@DeleteMapping("/customers/{id}")
	public HttpStatus deleteCustomer(@PathVariable long id) {
		this.customerService.deleteCustomer(id);
		return HttpStatus.OK;
	}
}
