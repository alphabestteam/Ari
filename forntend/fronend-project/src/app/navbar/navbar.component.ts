import { Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})

export class NavbarComponent implements OnInit {
  name: any

  ngOnInit(): void {
    this.getName()
  }
  getName() :void {
    this.name = sessionStorage.getItem("full_name")
  }
}
