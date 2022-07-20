$(document).ready(function() { //jesli strona sie zaladuje to wywolaj funkcj ponizej
    $.get("https://www.cheapshark.com/api/1.0/deals", function(data, status){ //wykonaj zapytanie na strone i wywolaj funkcje jak dostaniesz odpowiedz
        data.forEach(gra => { //dla kazdej gry z listy data wykonaj ponizsza funkcje
            // let gameHtml = "<tr><td>" + gra.title +"</td></tr>";
            // $("#gamesTable").append(gameHtml);

            let pic = $("<img class='game-img' src='" + gra.thumb + "'></img>");
            let img = $("<div></div>").append(pic);
            let title = $("<div name='title'></div>").html(gra.title);
            let price = $("<div name='price'></div>").html(gra.salePrice + "$");
            let rate = $("<div></div>").html(gra.steamRatingText == null ? "Brak oceny" : gra.steamRatingText);
            let iconHtml = "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-basket' viewBox='0 0 16 16'><path d='M5.757 1.071a.5.5 0 0 1 .172.686L3.383 6h9.234L10.07 1.757a.5.5 0 1 1 .858-.514L13.783 6H15a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1v4.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 13.5V9a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h1.217L5.07 1.243a.5.5 0 0 1 .686-.172zM2 9v4.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V9H2zM1 7v1h14V7H1zm3 3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3A.5.5 0 0 1 4 10zm2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3A.5.5 0 0 1 6 10zm2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3A.5.5 0 0 1 8 10zm2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3a.5.5 0 0 1 .5-.5zm2 0a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-1 0v-3a.5.5 0 0 1 .5-.5z'/></svg>"
            let button = $("<div><button name='addToBasket' class='btn btn-success'>" + iconHtml +"</button></div>");
            $(button).click(function() {
                let request_data = {"gameID" : gra.gameID};
                $.post("/api/basket", request_data, function(response_data, status){
                    console.log(response_data);
                    $(".toast-body").html("Added!")
                    $(".toast").show();
                })
            });
            let row = $("<div name='game' class='flex-item'></div>").append(img, title, price, rate, button);
            $("#games").append(row);
        });
      });

      $("#searchButton").click(function() {
          let searchValue = $("#search").val().toLowerCase(); //val() pobiera wartosc z inputa, jesli chcesz czegos innego wyciagnac to uzyj html()
          let searchPriceMin = parseFloat($("#priceMin").val()); //val() pobiera wartosc z inputa, jesli chcesz czegos innego wyciagnac to uzyj html()
          let searchPriceMax = parseFloat($("#priceMax").val());

          if(searchPriceMin != searchPriceMin) //bedzie true ale tylko w przypadku jak w searchPriceMin bedzie NaN (not a number)
          {
              searchPriceMin = 0;
          }

          if(searchPriceMax != searchPriceMax)
          {
              searchPriceMax = 0;
          }


         $("tr[name='game']").each(function(index) { //dla kazdego elementu z tagiem tr (czyli wiersza) zrob cos ponizej
               //this - element html, mozna na nim robic rzeczy z JS np zmienic styl, pobrac wartosc, innerHTML ale nie mozna zrobic na tym nic z jquery
               //zamienia element html na element jquery
               let title = $(this).find("td[name='title']")[0];
               let price = parseFloat($(this).find("td[name='price']")[0].innerHTML);

               console.log(title);
               if(searchValue == null || searchValue == "" || $(title).html().toLowerCase().includes(searchValue))
               {
                   if(price >= searchPriceMin && price <= searchPriceMax)
                   {
                       $(this).show();
                   }
                   else
                   {
                       $(this).hide(500);
                   }
               }
               else
               {
                   $(this).hide(500);
               }
         });
      });

      $("#basketBtn").click(function() {
              if ( $( "#basket" ).first().is( ":hidden" ) ) {
                $( "#basket" ).slideDown( "slow" );
              } else {
                $( "#basket" ).slideUp("slow");
              }
      });
});

//wybrac jakies api - np kurs złota albo kurs walut
//http://api.nbp.pl/
//załadować do tabelki
//dodać jakieś wyszukiwanie (ceny nizsze niz jakas wartos)
