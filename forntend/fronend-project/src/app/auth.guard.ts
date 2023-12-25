import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';


export const authGuard: CanActivateFn = (route, state) => {
  
  const session = sessionStorage.getItem('full_name');  
  const router = inject(Router)
    
  if (!session)  {
    router.navigate(['login'])
    return false
  } else {
    return true
  }
 };

