(() => {
    const forms = document.querySelectorAll('.form-delete');
  
    for (const form of forms) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
  
        const confirmed = confirm('Are you sure?');
  
        if (confirmed) {
          form.submit();
        }
      });
    }
})();

(() => {
  const ButtonShowMenu = document.querySelector('.button-show-menu');
  const ButtonCloseMenu = document.querySelector('.button-close-menu');
  const MenuContainer = document.querySelector('.menu-container');
  const MenuHidden = 'menu-hidden';
  const ButtonShowMenuVisible = 'button-show-menu-visible';

  const showMenu = () => {
    ButtonShowMenu.classList.remove(ButtonShowMenuVisible)
    MenuContainer.classList.remove(MenuHidden)
  };

  const closeMenu = () => {
    ButtonShowMenu.classList.add(ButtonShowMenuVisible)
    MenuContainer.classList.add(MenuHidden)
  };

  if(ButtonShowMenu){
    ButtonShowMenu.removeEventListener('click', showMenu)
    ButtonShowMenu.addEventListener('click', showMenu)
  };

  if(ButtonCloseMenu){
    ButtonCloseMenu.removeEventListener('click', closeMenu)
    ButtonCloseMenu.addEventListener('click', closeMenu)
  };
})();

(() => {
  const AuthorsLogoutLinks = document.querySelectorAll('.authors-logout-link');

  const FormLogout = document.querySelector('.form-logout');

  for(const link of AuthorsLogoutLinks){
    link.addEventListener('click', (e) => {
      e.preventDefault();
      FormLogout.submit();
    });
  }
})();