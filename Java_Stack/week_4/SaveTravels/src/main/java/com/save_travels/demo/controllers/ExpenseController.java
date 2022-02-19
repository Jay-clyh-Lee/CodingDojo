package com.save_travels.demo.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.save_travels.demo.models.Expense;
import com.save_travels.demo.services.ExpenseService;


@Controller
public class ExpenseController {

	@Autowired
	private ExpenseService service;
	
	@GetMapping("/")
	public String index() {
		
		return "redirect:/expenses";
	}
	
	@GetMapping("/expenses")
	public String home(
			@ModelAttribute("expense") Expense expense,
			Model model
			) {

		model.addAttribute("expenses", this.service.all());

		return "home.jsp";
	}
	
	// CREATE
	// create form
	@PostMapping("/expense/create")
	public String create(
			@Valid @ModelAttribute("expense") Expense expense,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if (result.hasErrors()) return "home.jsp";
		
		this.service.create(expense);
		
		redirectAttributes.addFlashAttribute("message", "A new expense has been added.");
		
		return "redirect:/expenses";
	}
	
	// READ
	@GetMapping("/expense/view/{id}")
	public String view(
			@PathVariable Long id,
			Model model
			) {
		
		model.addAttribute("expense", this.service.retrieve(id));
		
		return "viewExpense.jsp";
	}
	
	// EDIT
	// edit page
	@GetMapping("/expense/edit/{id}")
	public String edit(
			@PathVariable Long id,
			Model model
			) {
		
		model.addAttribute("expense", this.service.retrieve(id));
		
		return "editExpense.jsp";
	}
	
	// edit form
	@PostMapping("/expense/update/{id}")
	public String update(
			@Valid @ModelAttribute("expense") Expense expense,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if (result.hasErrors()) return "home.jsp";
		
		this.service.create(expense);
		
		redirectAttributes.addFlashAttribute("message", "A new expense has been added.");
		
		return String.format("redirect:/expense/view/%d", expense.getId());
	}
	
	//DELETE
	@GetMapping("/expense/delete/{id}")
	public String delete(
			@PathVariable Long id,
			RedirectAttributes redirectAttributes
			) {
		
		this.service.delete(id);
		
		redirectAttributes.addFlashAttribute("message", "This expense has been deleted");
		
		return "redirect:/expenses";		
	}
	
}
