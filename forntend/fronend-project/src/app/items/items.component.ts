import { Component } from '@angular/core';
import { ItemService } from '../item.service'
import { Router } from '@angular/router';
import { HttpClient, HttpEventType } from '@angular/common/http';
@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})

export class ItemsComponent {
  items: any[] = [];
  takenItems: any[] = [];
  // filterItems: any [] = []
  // homeCategory :any [] = []
  // workToolsCategory:any [] = []
  // officeCategory:any [] = []
  // generalCategory: any[] = []
  // elseCategory:any [] = []
  
  name: any
  admin : any

  selectedItemId: any;
  showDetails: boolean = false;
  
  constructor(private itemService: ItemService, private router: Router, private http:HttpClient ) { } 

  ngOnInit(): void {
    this.fetchItems();
    this.fetchTakenItems();
    this.getName()
    // this.filterItems = this.items
  }

  fetchItems(): void {
    this.itemService.getItems().subscribe(
      (data: any[]) => {
        this.items = data
          .filter(item => !item.taken)   
          .map((item) => ({ ...item, clicked: false }));
      },
      (error) => {
        console.error('Error fetching items:', error);
      }
    );
  }

  // homeItems(): void {
  //   this.itemService.getItems().subscribe(
  //     (data: any[]) => {
  //       this.filterItems = data
  //         .filter(item => item.item_category == "Home")   
  //         .map((item) => ({ ...item, clicked: false }));
  //     },
  //     (error) => {
  //       console.error('Error fetching items:', error);
  //     }
  //   );
  // }
  

  fetchTakenItems(): void {
    this.itemService.getTakenItems().subscribe(
      (data: any[]) => {
        this.takenItems = data.map((item) => ({ ...item, clicked: false }));
      },
      (error) => {
        console.error('Error fetching taken items:', error);
      }
    );
  }

  handleDivClick(item: any): void {
    this.selectedItemId = this.selectedItemId === item.id ? null : item.id;
    this.showDetails = this.selectedItemId !== null;
  }
  
  itemChosen = false
  selectedChosenItem: any;

  onClick(item: any): void {
    this.itemChosen = true;
    this.selectedChosenItem = item;
  }

  goToUpload(): void {
    this.router.navigate(['upload-items'])
  }

  getName() :void {
    this.name = sessionStorage.getItem("full_name")
    this.admin = sessionStorage.getItem("admin")
  }
  // selectedFile : File  = null;
  // onFileSelected(event: any) {
  // this.selectedFile = <File>event.target.files[0]
 }
  // onUpload() {
  //   const fd = new FormData();
  //   fd.append('image', this.selectedFile, this.selectedFile.name)
  //     this.http.post('', fd, {
  //       reportProgress: true,
  //       observe: 'events' 
  //     })
  //     .subscribe(event => {
  //       console.log(event);
  //     });
  // }
// }
