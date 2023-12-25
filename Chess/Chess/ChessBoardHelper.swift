//
//  ChessBoardHelper.swift
//  Chess
//
//  Created by Kaede Sugano on 22/12/2023.
//

import SwiftUI

struct ChessboardHelper {
    static func positionForRowAndColumn(row: Int, column: Int, cellWidth: CGFloat, cellHeight: CGFloat) -> CGPoint {
        let xPosition = screenWidth * 0.06 + cellWidth * CGFloat(column) + cellWidth / 2
        let yPosition = screenWidth * 0.08 + cellHeight * CGFloat(row) + cellHeight / 2
        return CGPoint(x: xPosition, y: yPosition)
    }

    static func columnLetter(from index: Int) -> String {
        let letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        return letters[index]
    }
    
    static func indexForButton(piece: ChessPiece) -> (row: Int, column: Int) {
        switch piece.side {
        case .white:
            return (row: 7 - piece.column, column: piece.row)
        case .black:
            return (row: 7 - piece.column, column: piece.row)
        case .none:
            return (-1, -1)
        }
    }
    
    static func getChessPosExp(piece: ChessPiece) -> String {
        let index = ChessboardHelper.indexForButton(piece: piece)
        return "\(ChessboardHelper.columnLetter(from: index.column))\(index.row + 1)"
    }
    
    static func opponentSide(side: ChessSide) -> ChessSide {
        if (side == .white) {
            return .black
        } else if (side == .black) {
            return .white
        }
        return .none
    }
}
