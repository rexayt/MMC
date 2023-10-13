
$(function () {


  // variáveis 
  const item = $('[data-anime]');
  

  //FIM da variáveis 

  // inicio carrossel 
  $('.carrossel-item').eq(0).addClass('active');
  var total = $('.carrossel-item').length;
  var current = 0;


  $('#moveRight').on('click', function () {
    var next = current;
    current = current + 1;
    setSlide(next, current);
  });


  $('#moveLeft').on('click', function () {
    var prev = current;
    current = current - 1;
    setSlide(prev, current);
  });




  function setSlide(prev, next) {
    var slide = current;
    if (next > total - 1) {
      slide = 0;
      current = 0;
    }

    if (next < 0) {
      slide = total - 1;
      current = total - 1;
    }

    $('.carrossel-item').eq(prev).removeClass('active');
    $('.carrossel-item').eq(slide).addClass('active');
    setTimeout(function () {

    }, 800);



    console.log('current ' + current);
    console.log('prev ' + prev);
  }

  // FIM do carrossel 


  // função para animação 
  const animeScroll = () => {
    const windowTop = $(window).scrollTop() + $(window).height() * 0.90;

    item.each(function(){
      if(windowTop > $(this).offset().top) {
        $(this).addClass('animate')
      }else{
        $(this).removeClass("animate")
      }
    })
  }


  $(window).scroll(function(){
    animeScroll()
  })

  animeScroll()

  // FIM da função para animaçãp 

});