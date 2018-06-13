mod.config(function ($routeProvider, $locationProvider) {

  $routeProvider
  .when('/', {
    title: 'FGC | Sistema - Menu',
    templateUrl: '/views/dashboard_times.html',
    controller: '',
    redirectTo: '/times',
  })

  //Times
  .when('/teams', {
    title: 'FGC | Sistema - Times',
    templateUrl: '/views/teams/times_list.html',
    controller: 'teamsList',
  })
  .when('/teams/new', {
    title: 'FGC | Sistema - Novo Time',
    templateUrl: '/views/teams/times_add.html',
    controller: 'teamsAdd',
  })
  .when('/teams/:times/edit', {
    title: 'FGC | Sistema - Editar Time',
    templateUrl: '/views/teams/times_add.html',
    controller: 'teamsAdd',
  })

  //Jogadores
  .when('/times', {
    title: 'FGC | Sistema - Jogadores',
    templateUrl: '/views/players/jogadores_list.html',
    controller: 'jogadorList',
  })
  .when('/times/new', {
    title: 'FGC | Sistema - Novo Jogador',
    templateUrl: '/views/players/jogadores_add.html',
    controller: 'jogadorAdd',
  })
  .when('/times/:times/edit', {
    title: 'FGC | Sistema - Editar Jogador',
    templateUrl: '/views/players/jogadores_add.html',
    controller: 'jogadorAdd',
  })
