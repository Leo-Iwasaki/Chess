//
//  ChessboardView.swift
//  Chess
//
//  Created by Kaede Sugano on 19/12/2023.
//

import SwiftUI

struct ChessboardView: View {
    let cellWidth: CGFloat
    let cellHeight: CGFloat
    let rows = 8
    let columns = 8
    let side: ChessSide
    
    init(screenWidth: CGFloat, side: ChessSide) {
        self.cellWidth = (screenWidth * 0.78) / CGFloat(columns) // Given that the board is a square
        self.cellHeight = (screenWidth * 0.75) / CGFloat(columns) // Given that the board is a square
        self.side = side
    }
    
    var body: some View {
        ZStack {
            Image(side == .white ? "w_board" : "b_board") // Make sure the "board" image is in your assets with this exact name
                .resizable()
                .scaledToFit()
                .frame(width: screenWidth * 0.9, height: screenWidth * 0.9)
            
            ForEach(0..<rows, id: \.self) { row in
                ForEach(0..<columns, id: \.self) { column in
                    Button(action: {
                        // Handle the button tap
                        let index = self.indexForButton(row: row, column: column)
                        print("Button at \(index.column), \(index.row) tapped")
                    }) {
                        Text("") // Empty text for invisible button
                            .frame(width: cellWidth, height: cellHeight)
                    }
                    .position(x: screenWidth * 0.06 + cellWidth * CGFloat(column) + cellWidth / 2,
                              y: screenWidth * 0.08 + cellHeight * CGFloat(row) + cellHeight / 2)
                }
            }
            .rotationEffect(.degrees(side == .white ? 180 : 0))

        }
        .frame(width: screenWidth * 0.9, height: screenWidth * 0.9)
    }
    
    private func indexForButton(row: Int, column: Int) -> (row: Int, column: Int) {
        switch side {
        case .white:
            return (row: 7 - column, column: row)
        case .black:
            return (row: 7 - column, column: row)
        }
    }

}
