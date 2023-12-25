import { Component, OnInit } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-upload-items',
  templateUrl: './upload-items.component.html',
  styleUrls: ['./upload-items.component.scss']
})
export class UploadItemsComponent {
  upload: any = {}
  id : any
  name : any
  ItemService: any;

  constructor(private itemService: ItemService, private router: Router) {}

    ngOnInit() {
      this.getName()
    }

    onSubmit(): void {
      this.upload.uploaded_by = this.id;
      this.itemService.uploadItems(this.upload)
        .subscribe(
          response => {
            console.log(response);
            if (response && response['user_exist']) {
              sessionStorage.setItem('full_name', response['user'].full_name);
              sessionStorage.setItem('user_id', response['user'].user_id);
              sessionStorage.setItem('email', response['user'].email);
            }
            alert('Item added successfully');
            this.goToHome();
          },
          error => {
            console.error('Upload failed', error);
          }
        );
    }
  
    goToHome() : void {
      this.router.navigate(['/home'])
    }

    getName(): void{
      this.name = sessionStorage.getItem("full_name")
      this.id = sessionStorage.getItem("user_id")
    }
   
}
