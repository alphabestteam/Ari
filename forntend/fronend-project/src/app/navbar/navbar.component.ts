import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  constructor(private router: Router) { }
  name: any
 
  ngOnInit(): void {
    this.getName()
  }
  getName() :void {
    this.name = sessionStorage.getItem("full_name")
  }
  logOut() {
    if (confirm("Are you sure you want to check out?")){
      window.sessionStorage.clear();
      this.router.navigate(["login"])
    }
  }

}
