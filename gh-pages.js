import { publish } from 'gh-pages';

publish(
 'build', // path to public directory
 {
  branch: 'gh-pages',
  repo: 'https://github.com/coder11235/aoc-2021-coder11235.git', // Update to point to your repository
  user: {
   name: 'coder11235', // update to use your name
   email: 'udaykalyansreenivasa@gmail.com' // Update to use your email
  },
  dotfiles: true
  },
  () => {
   console.log('Deploy Complete!');
  }
)
