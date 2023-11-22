import { Component } from '@angular/core';
import { FormControl, FormGroup, FormBuilder, Validators, FormArray } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  
  title = 'Form-Builder';
  isValid = false;
  profileForm = new FormGroup({
  username : new FormControl('',  [Validators.required, Validators.minLength(3)]),
  email : new FormControl('',  [Validators.required, Validators.email]),
  password : new FormControl('',  [Validators.required, Validators.minLength(8)])
  })

  onSubmit() {
    this.isValid = true
  }
}
















//   updateProfile() {
//   this.profileForm.patchValue({
//     address: {
//       street: '123 Drew Street'
//     }
//   });
// }
// get aliases() {
//   return this.profileForm.get('aliases') as FormArray;
// }
// addAlias() {
//   this.aliases.push(this.fb.control(''));
// }

// constructor(private fb: FormBuilder) { }
// }

