function menu() {
<<<<<<< HEAD
    document.getElementById("topnav").innerHTML = "<style>
    ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #343434;
    }
    li {
      float: left;
    }
    .dropbtn,
    li a {
      display: inline-block;
      color: #fff;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
    }
    .dropdown:hover .dropbtn,
    li a:hover {
      background-color: #86b300;
    }
    li.dropdown {
      display: inline-block;
    }
    .dropdown-content {
      display: none;
      position: absolute;
      background-color: #f9f9f9;
      min-width: 160px;
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
      z-index: 1;
    }
    .dropdown-content a {
      color: #000;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
      text-align: left;
      margin-left: 7px;
    }
    .dropdown-content a:hover {
      background-color: #f1f1f1;
    }
    .dropdown:hover .dropdown-content {
      display: block;
    }
    .bolder {
      font-weight: 900;
      color: blue !important;
      margin-left: 0px !important;
    }
  </style>
  <body>
    <ul>
      <li><a href="#">HOME</a></li>
      <li class="dropdown">
        <a
          href="https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html"
          class="dropbtn"
          >RADIOLOGIA TRADIZIONALE</a
        >
        <div class="dropdown-content">
          <a
            href="#"
            >Agenda & gestione della sala</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#refertazione-e-telefono"
            >Proiezioni radiografiche</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#densitometria-ossea"
            >Refertazione RX</a
          >
        </div>
      </li>
      <li class="dropdown">
        <a
          href="https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html"
          class="dropbtn"
          >CONTRASTOGRAFICI</a
        >
        <div class="dropdown-content">
          <a
            href="#"
            >Agenda & gestione della sala</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#refertazione-e-telefono"
            >Esecuzione dell'esame contastografico</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#densitometria-ossea"
            >Refertazione contrastografici</a
          >
        </div>
      </li>
      <li class="dropdown">
        <a
          href="https://sl-rad.github.io/SL-Rad-Vademecum/ecografia.html"
          class="dropbtn"
          >ECOGRAFIA</a
        >
        <div class="dropdown-content">
          <a href="#">Agenda & gestione della sala</a><a href="#">Esecuzione ecografia</a
          ><a href="#">Refertazione ecografia</a>
        </div>
      </li>
      <li class="dropdown">
        <a
          href="https://sl-rad.github.io/SL-Rad-Vademecum/tomografia_computerizzata.html"
          class="dropbtn"
          >TOMOGRAFIA COMPUTERIZZATA</a
        >
        <div class="dropdown-content">
          <a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/tomografia_computerizzata.html#gestione-agenda"
            >Agenda & gestione della sala</a
          ><a href="#">Manovre medico-infermieristiche</a>
          <a href="https://sl-rad.github.io/SL-Rad-Vademecum/tomografia_computerizzata.html#protocolli"
            >Protocolli di acquisizione TC</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/exam_flowchart/TC/flowchart_tc_generale.html"
            >Refertazione TC</a
          >
        </div>
      </li>
      <li class="dropdown">
        <a
          href="https://sl-rad.github.io/SL-Rad-Vademecum/risonanza_magnetica.html"
          class="dropbtn"
          >RISONANZA MAGNETICA</a
        >
        <div class="dropdown-content">
          <a href="#">Agenda & gestione della sala</a><a href="#">Manovre medico-infermieristiche</a><a href="#">Sequenze di acquisizione RM</a><a href="#">Refertazione RM</a>
        </div>
      </li>
      <li>
        <a href="https://sl-rad.github.io/SL-Rad-Vademecum/pronto_soccorso.html"
          >PRONTO SOCCORSO</a
        >
      </li>
  
      <li></li>
  
      <li class="dropdown">
        <a href="https://sl-rad.github.io/SL-Rad-Vademecum/contatti.html"
          >TELEFONI</a
        >
        <div class="dropdown-content">
          <a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/contatti.html#reparti"
            >Ambulatori e Reparti Ospedalieri</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/contatti.html#radiologia"
            >Radiologia Centrale</a
          ><a
            href="https://sl-rad.github.io/SL-Rad-Vademecum/contatti.html#pronto-soccorso"
            >Pronto Soccorso (DEA)</a
          >
        </div>
      </li>
    </ul>
    ";
=======
    document.getElementById("topnav").innerHTML = "<style>#topnav ul{list-style-type:none;margin:0;padding:0;overflow:hidden;background-color:#343434}#topnav li{float:left}.dropbtn,#topnav li a{display:inline-block;color:#fff;text-align:center;padding:14px 16px;text-decoration:none}#topnav .dropdown:hover .dropbtn,#topnav li a:hover{background-color:#86B300}#topnav li.dropdown{display:inline-block}#topnav .dropdown-content{display:none;position:absolute;background-color:#f9f9f9;min-width:160px;box-shadow:0 8px 16px 0 rgba(0,0,0,.2);z-index:1}#topnav .dropdown-content a{color:#000;padding:12px 16px;text-decoration:none;display:block;text-align:left;margin-left:7px}#topnav .dropdown-content a:hover{background-color:#f1f1f1}#topnav .dropdown:hover .dropdown-content{display:block}.bolder{font-weight:900;color:blue!important;margin-left:0px!important}</style><body><ul><li><a href='#'>Home</a></li><li class='dropdown'><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html' class='dropbtn'>Radiologia Tradizionale</a><div class='dropdown-content'><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#attivita-sala'>Attività sala</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#refertazione-e-telefono'>Refertazione e telefono</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#densitometria-ossea'>Densitometria ossea</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#esami-contrastografici'>Esami contrastografici</a><a class='bolder' href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#contrastografici'>Contrastografici</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#transitoesofago-gastrico'>Transito esofago-gastrico</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/radiologia_tradizionale.html#ileografia--rettografia'>Ileografia rettografia</a></div></li><li class='dropdown'><a href='https://sl-rad.github.io/SL-Rad-Vademecum/ecografia.html' class='dropbtn'>Ecografia</a><div class='dropdown-content'><a href='#'>Link 1</a><a href='#'>Link 2</a><a href='#'>Link 3</a></div></li><li class='dropdown'><a href='https://sl-rad.github.io/SL-Rad-Vademecum/tomografia_computerizzata.html' class='dropbtn'>Tomografia Computerizzata</a><div class='dropdown-content'><a href='https://sl-rad.github.io/SL-Rad-Vademecum/tomografia_computerizzata.html#gestione-agenda'>Agenda</a><a href='#'>Preparazione</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/tomografia_computerizzata.html#protocolli'>Protoccolli</a><a href='https://sl-rad.github.io/SL-Rad-Vademecum/exam_flowchart/TC/flowchart_tc_generale.html'>Refertazione</a></div></li><li class='dropdown'><a href='https://sl-rad.github.io/SL-Rad-Vademecum/risonanza_magnetica.html' class='dropbtn'>Risonanza Magnetica</a><div class='dropdown-content'><a href='#'>Link 1</a><a href='#'>Link 2</a><a href='#'>Link 3</a></div></li><li><a href='https://sl-rad.github.io/SL-Rad-Vademecum/pronto_soccorso.html'>Pronto soccorso</a></li><li><a href='https://sl-rad.github.io/SL-Rad-Vademecum/contatti.html'>Telefoni</a></li></ul>";
>>>>>>> parent of 39a821d (#NEW MENU REBOOT (REVERSE HERE))
}