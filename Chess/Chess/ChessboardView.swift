//
//  ChessboardView.swift
//  Chess
//
//  Created by Kaede Sugano on 19/12/2023.
//

import SwiftUI

struct ChessboardView: View {
    let side: ChessSide
    @ObservedObject var viewModel: ChessboardViewModel
    @EnvironmentObject var scrollViewTexts: MoveText
    
    init(side: ChessSide, viewModel: ChessboardViewModel) {
        self.side = side
        self.viewModel = viewModel
    }
    
    var body: some View {
        ZStack {
            Image(side == .white ? "w_board" : "b_board") // Make sure the "board" image is in your assets with this exact name
                .resizable()
                .scaledToFit()
                .frame(width: screenWidth * 0.9, height: screenWidth * 0.9)
                
            ForEach(0..<8, id: \.self) { row in
                ForEach(0..<8, id: \.self) { column in
                    PieceView(side: .white, row: row, column: column, viewModel: viewModel)
                        .environmentObject(scrollViewTexts)
                }
            }
                
        }
        .frame(width: screenWidth * 0.9, height: screenWidth * 0.9)
    }
}
