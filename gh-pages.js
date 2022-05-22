import { publish } from 'gh-pages';

publish(
 'build',// path to public directory
    {
        dotfiles: true
    },
  () => {
   console.log('Deploy Complete!');
  }
)
