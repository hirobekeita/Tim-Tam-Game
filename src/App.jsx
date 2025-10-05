import React, { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [sequence, setSequence] = useState([])
  const [gameStarted, setGameStarted] = useState(false)
  const [showResult, setShowResult] = useState(false)
  const [result, setResult] = useState(null)
  const [displayedSequence, setDisplayedSequence] = useState([])

  // ランダムなシーケンスを生成
  const generateRandomSequence = () => {
    const words = ['ティム', 'タム']
    const newSequence = []
    for (let i = 0; i < 13; i++) {
      newSequence.push(words[Math.floor(Math.random() * 2)])
    }
    return newSequence
  }

  // ゲームを開始
  const startGame = () => {
    const newSequence = generateRandomSequence()
    setSequence(newSequence)
    setDisplayedSequence([])
    setGameStarted(true)
    setShowResult(false)
  }

  // シーケンスを1つずつアニメーション表示
 useEffect(() => {
  if (gameStarted && displayedSequence.length < sequence.length) {
    // 7回目（インデックス6）の表示かどうかを判定
    const isSeventh = displayedSequence.length === 6;
    const delay = isSeventh ? 1000 : 350; // 7回目だけ1000ms、それ以外は350ms

    const timer = setTimeout(() => {
      setDisplayedSequence(prev => [...prev, sequence[prev.length]])
    }, delay);

    return () => clearTimeout(timer);
  }
}, [gameStarted, displayedSequence, sequence]);

  // ユーザーの推測を処理
  const makeGuess = (guess) => {
    if (!gameStarted) return

    // 正解を決定（ユーザーの推測の逆）
    const correctAnswer = guess === 'ティム' ? 'タム' : 'ティム'

    setResult({
      guess: guess,
      correct: correctAnswer,
      success: guess === correctAnswer
    })
    setShowResult(true)
  }

  // ゲームをリセット
  const resetGame = () => {
    setGameStarted(false)
    setSequence([])
    setDisplayedSequence([])
    setShowResult(false)
    setResult(null)
  }

  return (
    <div className="app-container">
      <div className="game-card">
        {/* タイトル */}
        <div className="title-bar">
          <h1>ティムタムゲーム</h1>
        </div>

        {/* 説明 */}
        <div className="info-section">
          <p>「ティム」と「タム」が13回表示されます。</p>
          <p>14回目に何がくるか当ててください！</p>
        </div>

        {/* シーケンス表示エリア */}
        <div className="sequence-area">
          {gameStarted ? (
            <>
              <div className="sequence-line">
                {displayedSequence.slice(0, 7).join('')}
              </div>
              <div className="sequence-line">
                {displayedSequence.slice(7, 13).join('')}
              </div>
            </>
          ) : (
            <div className="placeholder">
              ここにシーケンスが表示されます
            </div>
          )}
        </div>

        {/* ボタンエリア */}
        <div className="button-area">
          {!gameStarted ? (
            <button className="start-button" onClick={startGame}>
              ゲームスタート
            </button>
          ) : (
            <div className="answer-buttons">
              <button 
                className="answer-button tim-button"
                onClick={() => makeGuess('ティム')}
              >
                ティム
              </button>
              <button 
                className="answer-button tam-button"
                onClick={() => makeGuess('タム')}
              >
                タム
              </button>
            </div>
          )}
        </div>

        {/* 結果ダイアログ */}
        {showResult && result && (
          <div className="modal-overlay" onClick={resetGame}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
              <h2>結果</h2>
              <p className="result-text">
                正解は... <strong>{result.correct}</strong> でした！
              </p>
              <p className={result.success ? 'success' : 'failure'}>
                {result.success ? '当たりました！' : '残念！ハズレです！'}
              </p>
              <button className="ok-button" onClick={resetGame}>
                もう一度プレイ
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
