/*
Your job for today is to finish the sign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/

function sign(date){
        const month = date.getMonth(); 
        const day = date.getDate();
      
        switch (month) {
          case 0:
            sign = day <= 19 ? "Capricorn" : "Aquarius";
            break;
          case 1:
            sign = day <= 19 ? "Aquarius" : "Pisces";
            break;
          case 2:
            sign = day <= 20 ? "Pisces" : "Aries";
            break;
          case 3:
            sign = day <= 20 ? "Aries" : "Taurus";
            break;
          case 4:
            sign = day <= 21 ? "Taurus" : "Gemini";
            break;
          case 5:
            sign = day <= 21 ? "Gemini" : "Cancer";
            break;
          case 6:
            sign = day <= 22 ? "Cancer" : "Leo";
            break;
          case 7:
            sign = day <= 23 ? "Leo" : "Virgo";
            break;
          case 8:
            sign = day <= 23 ? "Virgo" : "Libra";
            break;
          case 9:
            sign = day <= 22 ? "Libra" : "Scorpio";
            break;
          case 10:
            sign = day <= 22 ? "Scorpio" : "Sagittarius";
            break;
          case 11:
            sign = day <= 21 ? "Sagittarius" : "Capricorn";
            break;
          default:
            sign = "Wrong date";
        }
      }
