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
        }
    }
}
