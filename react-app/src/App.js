import "./App.css";

function App() {
  return (
    <div className="App">
      <div id="navbar">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">
              Web Report
            </a>
            <button
              class="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNavAltMarkup"
              aria-controls="navbarNavAltMarkup"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div class="navbar-nav">
                <a class="nav-link active" aria-current="page" href="#">
                  Home
                </a>
                <a class="nav-link" href="#about">
                  ABOUT
                </a>
                <a class="nav-link" href="#works">
                  WORKS
                </a>
              </div>
            </div>
          </div>
        </nav>
      </div>
      <div class="content">
        <h2 class="">ABOUT</h2>
        <p class="">
          情報科学演習Ⅰでは主にSwiftを使用したAppの開発を行った。
          <br />
          自己紹介を含むApp開発ではUIKit、現在開発中の宗像市のApp開発ではSwiftUIやKotlinを使用して開発を行った。
          今まで意識してこなかったコードを理解するという過程を意識して行うことで、デバッグや機能を追加する際に効率的な作業が可能になった。
          <br />
          これまでで学んだことを活かし、自分の知らない言語や技術にも積極的に挑戦していきたい。
        </p>
      </div>
    </div>
  );
}

export default App;
