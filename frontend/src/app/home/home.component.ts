import { Component, OnInit } from '@angular/core';
import { gsap } from 'gsap';
import { Draggable } from 'gsap/Draggable';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
	// --------------------- VARIABLES ---------------------

	team = [
		{
			profile: '../assets/images/juan.jpg',
			names: 'Fernando Claudio',
			lastnames: 'Mamani Riqueza',
			email: 'fernando.mamani.50722@usalesiana.edu.bo',
			//linkedin: 'https://www.linkedin.com/in/juan-pablo-ortiz-rubio/',
			//github: 'https://github.com/jpablo-ortiz',
		},
	];

	// --------------------- CONSTRUCTOR ---------------------

	constructor() {}

	// ------------------- NgOn FUNCTIONS --------------------

	ngOnInit(): void {
		gsap.registerPlugin(ScrollTrigger, Draggable);
		// Init ScrollTrigger
		document.querySelectorAll('.box').forEach((box) => {
			const scrollBox = gsap.timeline({
				scrollTrigger: {
					trigger: box,
					pin: false,
					start: 'top center',
					end: 'center center',
					markers: false,
					toggleActions: 'play none none reverse',
				},
			});
			scrollBox.from(box, { y: 40, opacity: 0 });
		});
	}
}
