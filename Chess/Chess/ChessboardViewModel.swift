//
//  ChessboardViewModel.swift
//  Chess
//
//  Created by Kaede Sugano on 22/12/2023.
//

import SwiftUI

class ChessboardViewModel: ObservableObject {
    @Published var pieces: [[ChessPiece]] // 2D array representing the chess pieces
    
    init() {
        pieces = Array(repeating: Array(repeating: ChessPiece(name: " ", side: .black, row: 0, column: 0), count: 8), count: 8)
        
        for row in 0..<8 {
            for column in 0..<8 {
                pieces[row][column] = ChessPiece(name: " ", side: .black, row: row, column: column)
            }
        }
        
        // Pawns
        for column in 0..<8 {
            pieces[1][column] = ChessPiece(name: "p", side: .black, row: 1, column: column)
            pieces[6][column] = ChessPiece(name: "p", side: .white, row: 6, column: column)
        }
        
        // Rooks
        pieces[0][0] = ChessPiece(name: "r", side: .black, row: 0, column: 0)
        pieces[0][7] = ChessPiece(name: "r", side: .black, row: 0, column: 7)
        pieces[7][0] = ChessPiece(name: "r", side: .white, row: 7, column: 0)
        pieces[7][7] = ChessPiece(name: "r", side: .white, row: 7, column: 7)
        
        // Knights
        pieces[0][1] = ChessPiece(name: "n", side: .black, row: 0, column: 1)
        pieces[0][6] = ChessPiece(name: "n", side: .black, row: 0, column: 6)
        pieces[7][1] = ChessPiece(name: "n", side: .white, row: 7, column: 1)
        pieces[7][6] = ChessPiece(name: "n", side: .white, row: 7, column: 6)
        
        // Bishops
        pieces[0][2] = ChessPiece(name: "b", side: .black, row: 0, column: 2)
        pieces[0][5] = ChessPiece(name: "b", side: .black, row: 0, column: 5)
        pieces[7][2] = ChessPiece(name: "b", side: .white, row: 7, column: 2)
        pieces[7][5] = ChessPiece(name: "b", side: .white, row: 7, column: 5)
        
        // Kings
        pieces[0][4] = ChessPiece(name: "k", side: .black, row: 0, column: 4)
        pieces[7][4] = ChessPiece(name: "k", side: .white, row: 0, column: 4)
        
        // Queens
        pieces[0][3] = ChessPiece(name: "q", side: .black, row: 0, column: 3)
        pieces[7][3] = ChessPiece(name: "q", side: .white, row: 0, column: 3)
    }
    
    func movePiece(fromRow: Int, fromColumn: Int, toRow: Int, toColumn: Int) {
        guard fromRow >= 0, fromRow < pieces.count,
              fromColumn >= 0, fromColumn < pieces[fromRow].count,
              toRow >= 0, toRow < pieces.count,
              toColumn >= 0, toColumn < pieces[toRow].count else {
            return // Ensure indices are within bounds
        }
        
        let movingPiece = pieces[fromRow][fromColumn]
        let targetPiece = pieces[toRow][toColumn]

        // Swap the positions in the array
        pieces[toRow][toColumn] = movingPiece
        pieces[fromRow][fromColumn] = targetPiece
        
        // Update the row and column properties of the pieces
        pieces[toRow][toColumn].row = toRow
        pieces[toRow][toColumn].column = toColumn
        pieces[fromRow][fromColumn].row = fromRow
        pieces[fromRow][fromColumn].column = fromColumn
    }
}
